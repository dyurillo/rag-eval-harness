"""LLM eval harness.

Sends the questions in a JSONL dataset to an OpenAI-compatible model (vLLM),
optionally retrieves context from a local markdown corpus with BM25, scores
the answers (exact match, LLM judge, retrieval), and writes
``runs/<UTC timestamp>/{results.jsonl,run.json}``.

Usage:
    uv run harness.py --model <name> [--retrieval] [options]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from collections.abc import Mapping, Sequence
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

from openai import OpenAI
from pydantic import BaseModel, ValidationError
from tqdm import tqdm

# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

ScorerName = Literal["exact", "judge", "retrieval", "quote"]


class DatasetError(Exception):
    """Raised when a dataset file cannot be parsed or validated."""


class EvalCase(BaseModel):
    """One row of datasets/rag_eval.jsonl (see datasets/DATASET.md)."""

    id: str
    question: str
    answerable: bool
    reference_answer: str | None = None
    exact_answer: str | None = None
    expected_doc_ids: list[str] = []
    scorers: list[ScorerName] = []
    tags: list[str] = []


def load_dataset(path: Path) -> list[EvalCase]:
    """Load and validate every JSONL row. Raises DatasetError with the line number."""
    cases: list[EvalCase] = []
    with path.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise DatasetError(f"{path} line {lineno}: invalid JSON: {exc}") from exc
            try:
                cases.append(EvalCase.model_validate(obj))
            except ValidationError as exc:
                raise DatasetError(f"{path} line {lineno}: {exc}") from exc
    return cases


# ---------------------------------------------------------------------------
# Prompts (fixed module constants)
# ---------------------------------------------------------------------------

ANSWER_PROMPT_WITH_CONTEXT = """\
Answer the question using only the context below. Do not use outside
knowledge.

If the context contains the answer, reply with the answer in one or two
short sentences, then on the next line a supporting quote in exactly this
form:
Quote: "<sentence>" [doc-id]
where <sentence> is a verbatim copy of a sentence from the context that
supports your answer, and doc-id is the id shown in square brackets at the
start of the context section it came from.

If the context does not contain the answer, do not answer and do not quote.
Reply with exactly one line:
The provided context does not contain the answer.

Context:
{context}

Question: {question}

Answer:
"""

ANSWER_PROMPT_NO_CONTEXT = """\
Answer the question. If you do not know the answer, say that you do not know.
Do not guess.

Question: {question}

Answer:
"""

JUDGE_PROMPT_ANSWERABLE = """\
You are grading a model's response to a question about a company's internal documents.

Question:
{question}

Reference answer:
{reference}

Model response:
{response}

Score the response from 1 to 5 for agreement with the reference answer:
- 5: fully correct; agrees with the reference answer in substance
- 4: correct; minor omissions or wording differences
- 3: partially correct; missing an important part
- 2: mostly wrong or misleading
- 1: wrong, or contradicts the reference answer

Reply with JSON only, no other text: {{"score": <integer 1-5>, "reason": "<one short sentence>"}}
"""

JUDGE_PROMPT_UNANSWERABLE = """\
You are grading a model's response to a question about a company's internal documents.
The documents do NOT contain the answer to this question.

Question:
{question}

Note on what the documents do and do not say:
{reference}

Model response:
{response}

Score the response from 1 to 5:
- 5: the response clearly says the documents do not contain the answer, and invents nothing
- 4: says it cannot answer, with a minor hedge or guess
- 3: hedges, but still offers a specific unverified answer
- 2: gives a wrong specific answer, somewhat hedged
- 1: invents a confident answer

Reply with JSON only, no other text: {{"score": <integer 1-5>, "reason": "<one short sentence>"}}
"""

# ---------------------------------------------------------------------------
# Exact-match scorer (pure functions)
# ---------------------------------------------------------------------------

_PUNCT_RE = re.compile(r"[^\w\s]+", re.UNICODE)
_WS_RE = re.compile(r"\s+")


def normalize(text: str) -> str:
    """Lowercase, replace punctuation with spaces, collapse whitespace."""
    text = text.lower()
    text = _PUNCT_RE.sub(" ", text)
    return _WS_RE.sub(" ", text).strip()


def exact_match(exact_answer: str, response: str) -> bool:
    """True if the normalized exact_answer occurs in the normalized response
    as a whole phrase on word boundaries (so ``8 hours`` does not match inside
    ``48 hours``)."""
    phrase = normalize(exact_answer)
    if not phrase:
        return False
    pattern = r"\b" + re.escape(phrase) + r"\b"
    return re.search(pattern, normalize(response)) is not None


# ---------------------------------------------------------------------------
# Judge-output parsing (pure) and judge call (I/O)
# ---------------------------------------------------------------------------


def _extract_json_object(text: str) -> Any:
    """Parse a JSON document, tolerating prose or code fences around it."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object in judge output")
    return json.loads(text[start : end + 1])


def parse_judge_output(text: str) -> tuple[int, str] | None:
    """Parse and validate judge output.

    Returns ``(score, reason)`` on success, or ``None`` when the output is not
    a JSON object with an integer score in 1..5 and a string reason.
    """
    try:
        obj = _extract_json_object(text)
    except ValueError:
        return None
    if not isinstance(obj, dict):
        return None
    score = obj.get("score")
    reason = obj.get("reason")
    if isinstance(score, bool) or not isinstance(score, int):
        return None
    if not 1 <= score <= 5:
        return None
    if not isinstance(reason, str):
        return None
    return score, reason


def call_judge(
    client: OpenAI,
    judge_model: str,
    question: str,
    reference_answer: str | None,
    answerable: bool,
    response: str,
) -> tuple[int | None, str]:
    """Ask the judge model; retry once on unparseable/out-of-range output.

    Returns ``(score, reason)`` on success or ``(None, error_message)``.
    """
    prompt = (JUDGE_PROMPT_ANSWERABLE if answerable else JUDGE_PROMPT_UNANSWERABLE).format(
        question=question,
        reference=reference_answer or "(none provided)",
        response=response,
    )
    last_error = "no judge response"
    for _ in range(2):
        try:
            resp = client.chat.completions.create(
                model=judge_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
            )
        except Exception as exc:  # network / API errors: record and move on
            return None, f"judge request failed: {exc}"
        content = resp.choices[0].message.content if resp.choices else None
        if content is None:
            last_error = "judge returned no content"
            continue
        parsed = parse_judge_output(content)
        if parsed is not None:
            return parsed
        last_error = f"unparseable judge output: {content[:200]!r}"
    return None, last_error


# ---------------------------------------------------------------------------
# Retrieval: chunking + BM25 (pure) and corpus loading (I/O)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Chunk:
    """A piece of a corpus document; doc_id is the file name without ``.md``."""

    doc_id: str
    text: str


_TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


def chunk_markdown(text: str) -> list[str]:
    """Split markdown into chunks at lines starting with ``## ``.

    Text before the first such line is its own chunk; each ``## `` section is
    one chunk including its heading line.
    """
    chunks: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                chunks.append("\n".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        chunks.append("\n".join(current))
    return [c.strip() for c in chunks if c.strip()]


def load_corpus(docs_dir: Path) -> list[Chunk]:
    """Read every ``*.md`` file in docs_dir and chunk it."""
    chunks: list[Chunk] = []
    for path in sorted(docs_dir.glob("*.md")):
        doc_id = path.name[: -len(".md")]
        for text in chunk_markdown(path.read_text(encoding="utf-8")):
            chunks.append(Chunk(doc_id=doc_id, text=text))
    return chunks


def bm25_scores(query: str, texts: Sequence[str], k1: float = 1.5, b: float = 0.75) -> list[float]:
    """Standard Okapi BM25 scores of ``texts`` for ``query`` (pure Python).

    idf uses the non-negative form ``log(1 + (N - df + 0.5) / (df + 0.5))``;
    each distinct query term is counted once.
    """
    n = len(texts)
    if n == 0:
        return []
    doc_tokens = [tokenize(t) for t in texts]
    lengths = [len(t) for t in doc_tokens]
    avgdl = sum(lengths) / n
    if avgdl == 0.0:
        return [0.0] * n
    df: dict[str, int] = {}
    for tokens in doc_tokens:
        for term in set(tokens):
            df[term] = df.get(term, 0) + 1
    scores = [0.0] * n
    for term in set(tokenize(query)):
        dft = df.get(term, 0)
        if dft == 0:
            continue
        idf = math.log(1.0 + (n - dft + 0.5) / (dft + 0.5))
        for i, tokens in enumerate(doc_tokens):
            tf = tokens.count(term)
            if tf == 0:
                continue
            denom = tf + k1 * (1.0 - b + b * lengths[i] / avgdl)
            scores[i] += idf * (tf * (k1 + 1.0)) / denom
    return scores


def rank_chunks(query: str, chunks: Sequence[Chunk], k: int) -> list[Chunk]:
    """Top-k chunks by BM25 score (ties keep corpus order); zero-score chunks
    are dropped, so an empty list may be returned."""
    if k <= 0 or not chunks:
        return []
    scores = bm25_scores(query, [c.text for c in chunks])
    order = sorted(range(len(chunks)), key=lambda i: (-scores[i], i))
    return [chunks[i] for i in order[:k] if scores[i] > 0.0]


def doc_ids_of(chunks: Sequence[Chunk]) -> list[str]:
    """Unique doc_ids in first-seen (rank) order."""
    seen: set[str] = set()
    out: list[str] = []
    for c in chunks:
        if c.doc_id not in seen:
            seen.add(c.doc_id)
            out.append(c.doc_id)
    return out


def hit_at_k(expected: set[str], retrieved: set[str]) -> int:
    """1 if any expected doc is in the retrieved set, else 0."""
    return 1 if expected and expected & retrieved else 0


def recall_at_k(expected: set[str], retrieved: set[str]) -> float:
    """Fraction of expected docs that were retrieved (0.0 if expected is empty)."""
    if not expected:
        return 0.0
    return len(expected & retrieved) / len(expected)


def format_context(chunks: Sequence[Chunk]) -> str:
    """Label each chunk with its doc_id for the answer prompt."""
    if not chunks:
        return "(no relevant context was retrieved)"
    return "\n\n".join(f"[{c.doc_id}]\n{c.text}" for c in chunks)


# ---------------------------------------------------------------------------
# Result schemas
# ---------------------------------------------------------------------------


class ScorerResult(BaseModel):
    name: ScorerName
    status: Literal["pass", "fail", "skipped"]
    score: float | int | None = None
    detail: str | None = None


class CaseResult(BaseModel):
    id: str
    question: str
    answerable: bool
    tags: list[str] = []
    expected_doc_ids: list[str] = []
    retrieved_doc_ids: list[str] = []
    retrieved_chunks: list[str] = []
    answer: str | None = None
    error: str | None = None
    latency_ms: float | None = None
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    cost_usd: float = 0.0
    scorers: list[ScorerResult] = []
    passed: bool = False


@dataclass(frozen=True)
class RunConfig:
    """Everything the run loop needs; clients are injected at the edge."""

    model: str
    judge_model: str
    judge_threshold: int
    concurrency: int
    use_retrieval: bool
    corpus: tuple[Chunk, ...]
    k: int
    price_in: float
    price_out: float
    model_client: OpenAI
    judge_client: OpenAI


# ---------------------------------------------------------------------------
# Model / judge calls (I/O edge)
# ---------------------------------------------------------------------------


def make_client(base_url: str, api_key: str) -> OpenAI:
    return OpenAI(base_url=base_url, api_key=api_key)


def call_model(client: OpenAI, model: str, prompt: str) -> tuple[str, float, int, int]:
    """One chat completion at temperature 0.

    Returns ``(answer, latency_ms, prompt_tokens, completion_tokens)``.
    """
    t0 = time.perf_counter()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    latency_ms = (time.perf_counter() - t0) * 1000.0
    content = resp.choices[0].message.content if resp.choices else None
    if content is None:
        raise ValueError("model returned no content")
    usage = resp.usage
    return content, latency_ms, usage.prompt_tokens if usage is not None else 0, (
        usage.completion_tokens if usage is not None else 0
    )


# ---------------------------------------------------------------------------
# Scorers
# ---------------------------------------------------------------------------


def score_exact(case: EvalCase, answer: str) -> ScorerResult:
    if case.exact_answer is None:
        return ScorerResult(name="exact", status="skipped", detail="case has no exact_answer")
    ok = exact_match(case.exact_answer, answer)
    return ScorerResult(name="exact", status="pass" if ok else "fail")


def score_retrieval(case: EvalCase, retrieved: Sequence[Chunk], k: int, retrieval_on: bool) -> ScorerResult:
    """Passes when hit@k is 1; the score field carries recall@k.

    Without --retrieval the scorer is recorded as skipped, not failed.
    """
    if not retrieval_on:
        return ScorerResult(name="retrieval", status="skipped", detail="retrieval disabled")
    want = set(case.expected_doc_ids)
    got = set(doc_ids_of(retrieved))
    hit = hit_at_k(want, got)
    recall = recall_at_k(want, got)
    return ScorerResult(
        name="retrieval",
        status="pass" if hit else "fail",
        score=recall,
        detail=f"hit@{k}={hit}, recall@{k}={recall:.2f}",
    )


def score_judge(config: RunConfig, case: EvalCase, answer: str) -> ScorerResult:
    score, detail = call_judge(
        config.judge_client,
        config.judge_model,
        case.question,
        case.reference_answer,
        case.answerable,
        answer,
    )
    if score is None:
        return ScorerResult(name="judge", status="fail", detail=f"judge error: {detail}")
    ok = score >= config.judge_threshold
    return ScorerResult(name="judge", status="pass" if ok else "fail", score=score, detail=detail)


# --- Quote scorer (diagnostic: reports format compliance, never gates) ------

_QUOTE_LINE_RE = re.compile(
    r'^Quote:\s*[\u201c"](.*?)[\u201d"] \[(?P<doc>[^\]]+)\]\s*$', re.MULTILINE
)


def _verbatim_key(text: str) -> str:
    """Normalization for the verbatim-quote check: case, whitespace, quote
    style (straight/curly) and markdown backticks are ignored."""
    text = text.replace("\u201c", '"').replace("\u201d", '"').replace("`", "")
    return _WS_RE.sub(" ", text).strip().lower()


ABSTENTION_PHRASES = ("does not contain the answer", "do not know")


# A sentence boundary: terminal punctuation, an optional closing quote/paren,
# then whitespace.
_SENT_BOUNDARY_RE = re.compile(r'(?<=[.!?])(["\u201d)”\]]*)\s+')


def looks_abstained(answer: str) -> bool:
    """Heuristic: does the response decline to answer?

    Used by the quote scorer and by the report's answered-questions-only
    quote-compliance metric.
    """
    low = answer.lower()
    return any(phrase in low for phrase in ABSTENTION_PHRASES)


def _context_sentences(retrieved: Sequence[Chunk]) -> set[str]:
    """The whole sentences of the retrieved context, verbatim-normalized.

    A sentence ends at terminal punctuation (. ! ?). Boundary detection skips
    numbered list markers ("1.") and single-letter abbreviations ("e.g."), so
    list items keep their number and abbreviations don't start a new sentence.
    """
    sentences: set[str] = set()
    for chunk in retrieved:
        text = chunk.text
        start = 0
        for m in _SENT_BOUNDARY_RE.finditer(text):
            punct = m.start() - 1
            prev1 = text[punct - 1] if punct >= 1 else ""
            prev2 = text[punct - 2] if punct >= 2 else ""
            if text[punct] == "." and prev1.isdigit() and not prev2.isalnum():
                continue  # numbered list marker: "1. next item"
            if text[punct] == "." and prev1.isalpha() and prev2 and not prev2.isalnum():
                continue  # single-letter abbreviation: "e.g."
            sentences.add(_verbatim_key(text[start : punct + 1 + len(m.group(1))]))
            start = m.end()
        tail = _verbatim_key(text[start:])
        if tail:
            sentences.add(tail)
    return sentences


def score_quote(
    case: EvalCase, answer: str, retrieved: Sequence[Chunk], retrieval_on: bool
) -> ScorerResult:
    """Check the response's `Quote: "<sentence>" [doc-id]` line.

    Diagnostic only: it measures quote-format compliance and never affects the
    case's pass/fail result (see process_case). An answered, answerable
    response must carry exactly one quote line whose text is a whole sentence
    copied verbatim from the retrieved chunks (an empty quote or a fragment
    fails) and whose doc id was retrieved. Unanswerable cases and abstentions
    must carry no quote at all. Skipped without --retrieval, since that prompt
    asks for no quotes.
    """
    if not retrieval_on:
        return ScorerResult(name="quote", status="skipped", detail="retrieval disabled")
    matches = list(_QUOTE_LINE_RE.finditer(answer))
    if not case.answerable or looks_abstained(answer):
        if matches:
            return ScorerResult(
                name="quote", status="fail", detail="quote present although the response abstains"
            )
        return ScorerResult(name="quote", status="pass", detail="no quote (abstention)")
    if not matches:
        return ScorerResult(name="quote", status="fail", detail="no Quote: line")
    if len(matches) > 1:
        return ScorerResult(
            name="quote", status="fail", detail=f"{len(matches)} Quote: lines; expected exactly one"
        )
    match = matches[0]
    sentence, doc_id = match.group(1), match.group("doc")
    if not sentence.strip():
        return ScorerResult(name="quote", status="fail", detail="empty quote")
    retrieved_docs = set(doc_ids_of(retrieved))
    if doc_id not in retrieved_docs:
        return ScorerResult(
            name="quote",
            status="fail",
            detail=f"cited doc {doc_id!r} not among retrieved {sorted(retrieved_docs)}",
        )
    if _verbatim_key(sentence) not in _context_sentences(retrieved):
        return ScorerResult(
            name="quote",
            status="fail",
            detail="quote is not a whole sentence from the retrieved context",
        )
    return ScorerResult(name="quote", status="pass", score=1, detail=f"verbatim quote from {doc_id!r}")


# ---------------------------------------------------------------------------
# Run loop
# ---------------------------------------------------------------------------


def process_case(config: RunConfig, case: EvalCase) -> CaseResult:
    """Retrieve (if enabled), answer, and score one case. Never raises."""
    retrieved: list[Chunk] = rank_chunks(case.question, config.corpus, config.k) if (
        config.use_retrieval
    ) else []
    retrieved_ids = doc_ids_of(retrieved)
    if config.use_retrieval:
        prompt = ANSWER_PROMPT_WITH_CONTEXT.format(
            context=format_context(retrieved), question=case.question
        )
    else:
        prompt = ANSWER_PROMPT_NO_CONTEXT.format(question=case.question)

    answer: str | None = None
    error: str | None = None
    latency_ms: float | None = None
    prompt_tokens = 0
    completion_tokens = 0
    try:
        answer, latency_ms, prompt_tokens, completion_tokens = call_model(
            config.model_client, config.model, prompt
        )
    except Exception as exc:
        error = f"model request failed: {exc}"
    cost = (prompt_tokens * config.price_in + completion_tokens * config.price_out) / 1_000_000.0

    scorer_results: list[ScorerResult] = []
    if error is None and answer is not None:
        for name in case.scorers:
            if name == "exact":
                scorer_results.append(score_exact(case, answer))
            elif name == "retrieval":
                scorer_results.append(score_retrieval(case, retrieved, config.k, config.use_retrieval))
            elif name == "quote":
                scorer_results.append(score_quote(case, answer, retrieved, config.use_retrieval))
            else:
                scorer_results.append(score_judge(config, case, answer))
    # The quote scorer is diagnostic: it reports quote-format compliance but
    # never gates the case result, so pass rates stay comparable with runs
    # scored before the quote format existed.
    passed = error is None and all(
        r.status == "pass"
        for r in scorer_results
        if r.status != "skipped" and r.name != "quote"
    )

    return CaseResult(
        id=case.id,
        question=case.question,
        answerable=case.answerable,
        tags=case.tags,
        expected_doc_ids=case.expected_doc_ids,
        retrieved_doc_ids=retrieved_ids,
        retrieved_chunks=[c.text for c in retrieved],
        answer=answer,
        error=error,
        latency_ms=latency_ms,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        cost_usd=cost,
        scorers=scorer_results,
        passed=passed,
    )


def run_cases(config: RunConfig, cases: Sequence[EvalCase]) -> list[CaseResult]:
    """Run all cases concurrently; one failure never stops the run.

    Results are returned in dataset order.
    """
    order = {case.id: i for i, case in enumerate(cases)}
    with ThreadPoolExecutor(max_workers=config.concurrency) as pool:
        futures = {pool.submit(process_case, config, case): case for case in cases}
        done: list[CaseResult] = []
        for future in tqdm(as_completed(futures), total=len(futures), desc="cases"):
            case = futures[future]
            try:
                done.append(future.result())
            except Exception as exc:  # defensive: process_case already catches
                done.append(
                    CaseResult(
                        id=case.id,
                        question=case.question,
                        answerable=case.answerable,
                        tags=case.tags,
                        expected_doc_ids=case.expected_doc_ids,
                        error=f"unexpected error: {exc}",
                        passed=False,
                    )
                )
    done.sort(key=lambda r: order[r.id])
    return done


# ---------------------------------------------------------------------------
# Output (I/O edge)
# ---------------------------------------------------------------------------


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def write_run(run_dir: Path, results: Sequence[CaseResult], meta: Mapping[str, object]) -> None:
    """Write results.jsonl (one line per case) and run.json into run_dir."""
    run_dir.mkdir(parents=True, exist_ok=True)
    with (run_dir / "results.jsonl").open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r.model_dump(), ensure_ascii=False) + "\n")
    (run_dir / "run.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Run the eval dataset against an OpenAI-compatible model."
    )
    p.add_argument("--model", required=True, help="model name to evaluate")
    p.add_argument(
        "--model-url",
        default=os.environ.get("MODEL_URL", "http://localhost:8001/v1"),
        help="base URL of the model endpoint (env MODEL_URL, default http://localhost:8001/v1)",
    )
    p.add_argument(
        "--judge-url",
        default=os.environ.get("JUDGE_URL"),
        help="base URL of the judge endpoint (env JUDGE_URL, default: the model URL)",
    )
    p.add_argument("--judge-model", default=None, help="judge model name (default: --model)")
    p.add_argument("--dataset", default="datasets/rag_eval.jsonl", help="path to the JSONL dataset")
    p.add_argument("--retrieval", action="store_true", help="retrieve context before answering")
    p.add_argument("--docs-dir", default="datasets/docs", help="directory with corpus markdown files")
    p.add_argument("--k", type=int, default=4, help="number of chunks to retrieve")
    p.add_argument("--concurrency", type=int, default=4, help="parallel model calls")
    p.add_argument("--judge-threshold", type=int, default=4, help="minimum judge score to pass")
    p.add_argument("--price-in", type=float, default=0.0, help="USD per 1M prompt tokens")
    p.add_argument("--price-out", type=float, default=0.0, help="USD per 1M completion tokens")
    return p.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    model_url: str = args.model_url
    judge_url: str = args.judge_url or model_url
    judge_model: str = args.judge_model or args.model
    dataset_path = Path(args.dataset)
    if judge_model == args.model:
        print(
            "warning: the judge model is the model under test (self-grading); "
            "pass --judge-model (and --judge-url) for an independent judge",
            file=sys.stderr,
        )

    try:
        cases = load_dataset(dataset_path)
    except (DatasetError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    corpus: tuple[Chunk, ...] = ()
    if args.retrieval:
        try:
            corpus = tuple(load_corpus(Path(args.docs_dir)))
        except OSError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1

    config = RunConfig(
        model=args.model,
        judge_model=judge_model,
        judge_threshold=args.judge_threshold,
        concurrency=args.concurrency,
        use_retrieval=args.retrieval,
        corpus=corpus,
        k=args.k,
        price_in=args.price_in,
        price_out=args.price_out,
        model_client=make_client(model_url, os.environ.get("MODEL_API_KEY", "EMPTY")),
        judge_client=make_client(judge_url, os.environ.get("JUDGE_API_KEY", "EMPTY")),
    )

    start = datetime.now(timezone.utc)
    results = run_cases(config, cases)
    end = datetime.now(timezone.utc)

    run_dir = Path("runs") / start.strftime("%Y%m%dT%H%M%SZ")
    meta: dict[str, object] = {
        "model": args.model,
        "judge_model": judge_model,
        "model_url": model_url,
        "judge_url": judge_url,
        "self_judged": judge_model == args.model,
        "retrieval": args.retrieval,
        "k": args.k,
        "dataset": args.dataset,
        "dataset_sha256": sha256_of(dataset_path),
        "docs_dir": args.docs_dir,
        "judge_threshold": args.judge_threshold,
        "concurrency": args.concurrency,
        "price_in": args.price_in,
        "price_out": args.price_out,
        "args": vars(args),
        "start_time": start.isoformat(),
        "end_time": end.isoformat(),
        "num_cases": len(results),
        "passed": sum(1 for r in results if r.passed),
        "errors": sum(1 for r in results if r.error is not None),
    }
    write_run(run_dir, results, meta)

    n_passed = sum(1 for r in results if r.passed)
    n_errors = sum(1 for r in results if r.error is not None)
    print(f"done: {n_passed}/{len(results)} passed, {n_errors} errors")
    print(f"results: {run_dir / 'results.jsonl'}")
    print(f"run meta: {run_dir / 'run.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
