# rag-eval-harness

> [!NOTE]
> Adapted with permission from work I did at Solstice Software Solutions (2025–2026). After leaving in June 2026, I extended it independently and re-ran every result below in October 2026.

A small eval harness for a model served by vLLM (any OpenAI-compatible
endpoint) on a local RAG task. It sends the 48 questions of a local dataset
to the model under test, optionally retrieves context from a 12-document
corpus with an in-process BM25 retriever, scores the answers with four
scorers (exact match, LLM judge, retrieval, and a diagnostic quote-format
check), and writes a per-run directory with machine-readable results plus a
markdown/HTML report.

Plain functions, standard library plus `openai`, `pydantic`, `jinja2`, and
`tqdm`. No framework or external retrieval service is required: BM25 runs
in-process, while model and judge calls use OpenAI-compatible endpoints.

The harness was built to grade the companion LoRA fine-tune repository
([training repo](https://github.com/dyurillo/gemma-3-rag-finetuning)):
base vs. adapter, with and without retrieval (k = 1/2/4). The results
below are from that comparison.

## Results

Dataset: `datasets/rag_eval.jsonl` (sha256 `3656204d…`): 48 questions —
42 answerable (30 of them exact-match scored) and 6 unanswerable — over 12
synthetic documents chunked into 80 BM25 chunks. Judge:
`Qwen/Qwen3.8-27B-FP8`, passing at ≥ 4 of 5. All runs at temperature 0,
0 errors.

**Overall pass rate (n = 48)**

| model | no retrieval | k = 1 | k = 2 | k = 4 |
|---|---|---|---|---|
| `google/gemma-3-1b-it` (base) | 7 | 25 | 28 | 30 |
| 1B + LoRA adapter (sentence targets) | 6 | 26 | 25 | 27 |

These results come from the eight runs committed in
[results/](results/): base and adapter, closed-book and k = 1/2/4. Each
run has per-case outputs, run metadata, and a rendered report.

The adapter's pass rate trails the base in three of four cells and is
one case ahead at k = 1 (26 vs 25): k = 4 is 27 vs 30, k = 2 is 25 vs
28, and no retrieval is 6 vs 7.
Re-runs of a cell drift by ±1–2 — about the size of the 3-case gap at
k = 4. Because both models are evaluated on the same 48 questions and
the sample is small, treat this comparison as descriptive; no inferential
significance claim is made here.

**What the fine-tune did change (k = 4)**

| metric | base | 1B + LoRA |
|---|---|---|
| overall pass rate | 30/48 | 27/48 |
| verbatim quote compliance (all 48 cases) | 14/48 (29%) | 45/48 (94%) |
| verbatim quote compliance (answered questions only)¹ | 3/37 (8%) | 32/35 (91%) |
| unanswerable abstention (n = 6) | 6/6 | 6/6 |

¹ The 42 answerable questions minus the model's abstentions (base 5,
adapter 7): format compliance when the model actually answers. The 6
unanswerable questions are excluded. The base count includes one case
whose malformed quote line quoted the prompt's abstention sentence and so
was read as an abstention.

- **Format.** The base model's 34 quote misses at k = 4 split into 14
  answers with no quote line at all, 15 with a quote but no doc id, and 5
  carrying the literal `[doc-id]` (one also `<sentence>`) placeholder.
  The adapter produces the required `Quote: "<verbatim sentence>" [doc-id]`
  line in essentially every answer; its 3 misses are a recited product
  list with no quote line, and two quotes where a backtick code span was
  rendered with double quotes, breaking the verbatim check.
- **Abstention.** 6/6 with retrieval at k = 4 for both models. With less
  context both fall for near-miss traps: the base on the battery-procedure
  question (it recites Tag v3 specs instead of abstaining), the adapter on
  the cloud-provider, IC-stipend and shipment-count questions (it answers
  from the adjacent fact in the chunk). Closed-book, both models
  deterministically hallucinate "AWS" on the provider question.
- **Accuracy.** What the adapter loses is reading comprehension, not
  format: it recites the first sentence or first table row of a chunk
  instead of localizing the answer fact (see Failure analysis).

## Failure analysis

From case-by-case review of the final runs, both models, all k:

- **Format / quote** — fixed by the adapter: missing quote line, a quote
  line without a doc id, literal `[doc-id]`/`<sentence>` placeholders, a
  quote altered from the context (a comma, an apostrophe, or a code span
  rendered with double quotes), and — mostly at low k — a quote attached
  to an abstention or to a hallucinated near-miss answer.
- **Recite-from-top** — the 1B ceiling, in both models and the adapter's
  dominant error at k = 4: instead of finding the relevant line it recites
  the chunk's opening — the adapter at k = 4 recites the rotation-structure
  sentences instead of "Tuesdays 10:00 Central" for the on-call handoff
  question, the wrong row of the SLA table, and the whole six-step
  pipeline instead of the two carrier names; the base model shows the same
  at k = 1/2 (the data-flow list instead of the carrier names).
- **Near-miss hallucination** — when a retrieved chunk mentions an
  adjacent fact (a region name, an IC rotation, a 2020 pilot shipment),
  the model answers with that. Concentrated in the unanswerables — all
  three near-miss traps, plus the 2025-shipment-count question falling for
  the 2020-pilot fact — and more frequent with less context: the adapter
  abstains 6/6 at k = 4 but only 4/6 at k = 2 and 5/6 at k = 1 and
  closed-book.
- **Over-abstention** — the fine-tuned model sometimes declines an answer
  that is in the retrieved context (at k = 4: the RPO/RTO values, the
  normalizer replica ceiling, the 72-hour offline buffer, the IC/debugger
  rule, and the Platform rotation's coverage); the base model got the
  RPO/RTO, replica-ceiling and rotation-coverage cases right.
- **Irreducible** — failed by both models: two-hop multi-document
  questions (the answer needs two docs, retrieval must surface both),
  derived arithmetic (excursion timing = 3 consecutive readings × 90 s),
  the wrong-service trap, and plain retrieval misses at low k.

Run-to-run noise is ±1–2 per cell (judge + vLLM scheduling), about the
size of the 3-case base-vs-adapter gap at k = 4. The adapter trails the
base in three of four cells and leads by one case at k = 1; these
differences are descriptive, not statistically meaningful.

## Layout

- `harness.py` — dataset loading/validation, chunking + BM25, model and
  judge calls, scorers, and the run loop; writes structured results locally
- `report.py` — renders Markdown and self-contained HTML summaries for a
  local run
- `deepeval_check.py` — optional cross-check with DeepEval's RAG metrics
  (G-Eval correctness, faithfulness, contextual recall), using the same
  local judge; writes its output locally
- `datasets/` — the 12 documents, 48 questions and the consistency checker
  (see `datasets/DATASET.md`)
- `tests/` — pytest tests (no network access)
- `runs/` — ignored raw per-run outputs
- [`results/`](results/) — the eight runs behind the results table (per-case
  results, run metadata, reports, and DeepEval scores at k = 1)

## Setup

For the optional Nix/direnv environment, copy `.envrc.example` to `.envrc`,
review the defaults, then run `direnv allow`. Keep machine-specific values
and credentials in the ignored `.env` file, never in the example. You can
also set the environment variables manually.

Requires Python 3.12. Dependencies are pinned in `pyproject.toml` /
`uv.lock`:

```sh
uv lock
uv sync --locked
```

Configuration is via CLI flags and environment variables:

- `--model` (required): name of the model under test, as served by the
  endpoint.
- `--model-url`: base URL, default `$MODEL_URL`, then
  `http://localhost:8001/v1` (the runs above used :8001 for the model and
  :8000 for the judge).
- `--judge-url`: base URL for the judge, default `$JUDGE_URL`, then the
  model URL.
- `--judge-model`: judge model name, default `--model` (self-grading: the
  harness prints a warning and records this in the run metadata).
- API keys: `MODEL_API_KEY` and `JUDGE_API_KEY` env vars (default `EMPTY`,
  which vLLM accepts).

## Dataset check

After touching anything under `datasets/`, run the consistency checks:

```sh
uv run datasets/check_dataset.py
```

## Tests

No network needed:

```sh
uv run pytest
```

## Running the harness

New runs are written to `runs/`, which is git-ignored. `make_results.py`
copies the runs behind the README into `results/`. Each run records per-case
results and run metadata, including model and judge settings, retrieval
configuration, dataset hash, and timestamps.

Closed-book (no retrieval):

```sh
uv run harness.py --model <model>
```

With retrieval (top-k BM25 chunks from `datasets/docs`):

```sh
uv run harness.py --model <model> --retrieval
uv run harness.py --model <model> --retrieval --k 1
```

Useful options (defaults in parentheses):

- `--dataset` (datasets/rag_eval.jsonl), `--docs-dir` (datasets/docs)
- `--k` (4), `--concurrency` (4), `--judge-threshold` (4)
- `--price-in` / `--price-out` (0, 0) — USD per 1M tokens, for the cost
  column
- `--judge-url`, `--judge-model` — use a different judge endpoint/model

A failing model request never stops the run: the case is recorded with an
`error` field and the loop continues.

## Report

After a run, render the report into that run's directory:

```sh
uv run report.py <local-run-directory>
```

This writes a self-contained Markdown and HTML report (inline CSS, no JS,
no external assets). The report shows the run header (model, judge,
retrieval, k), a summary (overall and per-scorer/per-tag pass rates, mean
judge score, hallucination rate, retrieval hit@k / recall@k, latency
p50/p95, total tokens and cost, quote compliance over answered questions
only, error count), a per-question table, and
every failed case with its question, response, retrieved docs and judge
reason.

## Cross-check with DeepEval

Optional, for one run at a time. It scores each answerable, retrieved case
with DeepEval — G-Eval **correctness** (compared case-by-case with the
harness's own judge), **faithfulness** (are the answer's claims supported
by the retrieved chunks) and **contextual recall** (a chunk-level view of
retrieval, unlike the harness's doc-level hit@k):

```sh
uv run --group deepeval python deepeval_check.py <local-run-directory> \
    --judge-model Qwen/Qwen3.8-27B-FP8
```

Fully local: telemetry opt-out, read-only file system, no API key.

Across the locally generated k = 1 base/adapter comparison (42
answerable cases per model), DeepEval's G-Eval correctness (threshold 0.75,
compared with the harness's 4/5 pass threshold) agrees with the harness
judge in **74/84 cases (88%)**: **36/42 (86%)** for base and **38/42 (90%)**
for the adapter. The 10 disagreements are cases where the harness judge
passed but DeepEval scored correctness 0.6–0.7. These figures come from
[results/base-k1/deepeval.jsonl](results/base-k1/deepeval.jsonl) and
[results/adapter-k1/deepeval.jsonl](results/adapter-k1/deepeval.jsonl).

## Scorers

A case lists which scorers apply in its `scorers` field. A case passes
when every scorer that ran on it passed; skipped scorers don't count.

- **exact** — normalizes both the `exact_answer` span and the response
  (lowercase, punctuation replaced with spaces, whitespace collapsed), then
  checks that the span occurs in the response as a whole phrase on word
  boundaries, so `8 hours` does not match inside `48 hours`. Skipped if
  the case has no `exact_answer`.
- **judge** — sends the question, the reference answer, the `answerable`
  flag and the response to the judge model with a fixed 1–5 rubric
  (agreement with the reference for answerable cases; for unanswerable
  cases 5 = clearly says the docs don't contain the answer, 1 = invents
  one) and requires JSON output `{"score": int, "reason": str}`. Passes if
  the score is at least `--judge-threshold` (default 4). Unparseable or
  out-of-range output is retried once; if it still fails, the case's judge
  score is recorded as null with an error and the scorer counts as failed.
- **retrieval** — the retrieved doc set is the unique doc ids among the
  top-k chunks. hit@k is 1 if any expected doc is in the set; recall@k is
  the fraction of expected docs in it. The scorer passes when hit@k is 1
  and reports recall@k. Without `--retrieval` it is recorded as skipped,
  not failed.
- **quote** (diagnostic) — checks the quote line the answer prompt
  requires: an answered response must carry exactly one
  `Quote: "<sentence>" [doc-id]` line whose text is a **whole sentence**
  copied verbatim from the retrieved chunks (an empty quote or a fragment
  fails) and whose doc id was retrieved; unanswerable cases and abstentions
  must carry no quote at all. It never gates the
  case result — pass/fail is decided by the other scorers only, so pass
  rates stay comparable with runs scored before the quote format existed.
  Without `--retrieval` it is recorded as skipped.

Retrieval itself: corpus files are chunked at `## ` headings (the intro
before the first heading is its own chunk; a chunk's doc id is the file
name without `.md`), ranked with a pure-Python Okapi BM25 (token regex
`[a-z0-9]+`, k1=1.5, b=0.75, non-negative idf form), and the top-k chunks
are included in the answer prompt labelled with their doc ids. The answer
prompt instructs the model to answer in one or two short sentences and
then add a verbatim supporting quote line `Quote: "<sentence>" [doc-id]`;
when the context lacks the answer it must reply with the single
abstention line and no quote (without retrieval, to say it doesn't know);
temperature is 0 throughout.

## Dataset

The 12 synthetic documents (a fictional company's on-call, incident,
deploy, runbook, architecture, retention, access, expense, PTO and
support policies), the 48 questions, the labeling rules and the known
limitations are documented in [datasets/DATASET.md](datasets/DATASET.md) —
see that file instead of re-reading the questions here.

## Limitations

- 48 questions, so each cell has wide error bars (±1–2 between runs of
  the same cell).
- One 27B judge model; rubric noise is the dominant variance source.
- BM25 only — no embedding or reranker baseline.
- The corpus is synthetic and single-domain (policies and runbooks).
