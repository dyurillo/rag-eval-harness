"""Cross-check one harness run with DeepEval's RAG metrics, using the same local judge.

For each answerable case answered with retrieval, DeepEval scores:
  correctness        G-Eval: does the answer agree with the reference answer?
                     Compared case by case with the harness's own judge.
  faithfulness       Are the answer's claims supported by the retrieved chunks?
  contextual_recall  Do the retrieved chunks contain what the reference answer needs?
                     (a chunk-level view of retrieval, unlike the harness's doc-level hit@k)

Usage:
    uv run --group deepeval python deepeval_check.py runs/<timestamp> \\
        --judge-model Qwen/Qwen3.8-27B-FP8

Writes runs/<timestamp>/deepeval.jsonl and prints a summary. Needs the harness to
record each case's retrieved chunk texts as `retrieved_chunks` in results.jsonl.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

# Keep DeepEval local: no telemetry, no Confident AI uploads, no cache files in the repo.
# These must be set before deepeval is imported.
os.environ.setdefault("DEEPEVAL_TELEMETRY_OPT_OUT", "1")
os.environ.setdefault("DEEPEVAL_FILE_SYSTEM", "READ_ONLY")
os.environ.pop("CONFIDENT_API_KEY", None)

from deepeval.metrics import (  # noqa: E402 (needs the settings above)
    BaseMetric,
    ContextualRecallMetric,
    FaithfulnessMetric,
    GEval,
)
from deepeval.models import LocalModel  # noqa: E402
from deepeval.test_case import (  # noqa: E402
    LLMTestCase,
    RetrievedContextData,
    SingleTurnParams,
)

# The harness judge passes at 4 on its 1-5 scale; (4 - 1) / (5 - 1) = 0.75 on DeepEval's 0-1 scale.
CORRECTNESS_THRESHOLD = 0.75
CORRECTNESS_CRITERIA = (
    "Decide whether the actual output agrees in substance with the expected output, which is "
    "the reference answer. Penalize missing key facts and contradictions. Do not penalize extra "
    "correct detail or a supporting quote."
)

Row = dict[str, Any]


def load_jsonl(path: Path) -> list[Row]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def chunk_texts(row: Row) -> list[str | RetrievedContextData]:
    """The retrieved chunks' text, in rank order, as DeepEval's retrieval_context.

    Typed as DeepEval declares the field: list is invariant, so a plain list[str]
    would not type-check against list[str | RetrievedContextData].
    """
    chunks = row.get("retrieved_chunks")
    if chunks is None:
        sys.exit(
            "results.jsonl has no 'retrieved_chunks'. Make the harness record each case's "
            "retrieved chunk texts, then re-run the harness for this run."
        )
    return [c["text"] if isinstance(c, dict) else str(c) for c in chunks]


def harness_judge_status(row: Row) -> str | None:
    """The harness judge's verdict for this case: "pass", "fail", "skipped", or None."""
    judge = next((s for s in row["scorers"] if s.get("name") == "judge"), None)
    return judge.get("status") if judge else None


def build_metrics(judge: LocalModel) -> dict[str, BaseMetric]:
    correctness = GEval(
        name="Correctness",
        criteria=CORRECTNESS_CRITERIA,
        evaluation_params=[
            SingleTurnParams.INPUT,
            SingleTurnParams.ACTUAL_OUTPUT,
            SingleTurnParams.EXPECTED_OUTPUT,
        ],
        threshold=CORRECTNESS_THRESHOLD,
        model=judge,
    )
    return {
        "correctness": correctness,
        "faithfulness": FaithfulnessMetric(model=judge),
        "contextual_recall": ContextualRecallMetric(model=judge),
    }


def score_case(row: Row, reference: str, metrics: dict[str, BaseMetric]) -> Row:
    """Run every metric on one case. A malformed judge reply fails that metric, not the run."""
    case = LLMTestCase(
        input=row["question"],
        actual_output=row["answer"],
        expected_output=reference,
        retrieval_context=chunk_texts(row),
    )
    record: Row = {"id": row["id"], "harness_judge": harness_judge_status(row)}
    for name, metric in metrics.items():
        try:
            metric.measure(case)
            record[name] = metric.score
            record[f"{name}_reason"] = metric.reason
        except (
            Exception
        ) as exc:  # record and continue: one bad reply shouldn't stop the run
            record[name] = None
            record[f"{name}_error"] = str(exc)[:300]
    return record


def mean(records: list[Row], name: str) -> str:
    values = [r[name] for r in records if r[name] is not None]
    return f"{sum(values) / len(values):.2f} (n={len(values)})" if values else "n/a"


def print_summary(records: list[Row]) -> None:
    compared = [
        r
        for r in records
        if r["correctness"] is not None and r["harness_judge"] in ("pass", "fail")
    ]
    disagree = [
        r
        for r in compared
        if (r["correctness"] >= CORRECTNESS_THRESHOLD) != (r["harness_judge"] == "pass")
    ]
    print(f"\ncases scored:        {len(records)}")
    print(f"mean correctness:    {mean(records, 'correctness')}")
    print(f"mean faithfulness:   {mean(records, 'faithfulness')}")
    print(f"mean context recall: {mean(records, 'contextual_recall')}")
    if compared:
        agreed = len(compared) - len(disagree)
        print(
            f"judge agreement:     {agreed}/{len(compared)} ({agreed / len(compared):.0%}) "
            "harness judge vs DeepEval correctness, pass/fail"
        )
    for r in disagree:
        print(
            f"  disagree {r['id']}: harness {r['harness_judge']}, DeepEval {r['correctness']:.2f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "run_dir", type=Path, help="a harness run directory, e.g. runs/20261022T040900Z"
    )
    parser.add_argument("--dataset", type=Path, default=Path("datasets/rag_eval.jsonl"))
    parser.add_argument(
        "--judge-url", default=os.environ.get("JUDGE_URL", "http://localhost:8000/v1")
    )
    parser.add_argument("--judge-model", required=True)
    args = parser.parse_args()

    references = {r["id"]: r["reference_answer"] for r in load_jsonl(args.dataset)}
    rows = [
        r
        for r in load_jsonl(args.run_dir / "results.jsonl")
        if r["answerable"] and r.get("answer") and r.get("retrieved_doc_ids")
    ]
    if not rows:
        sys.exit(
            "no answerable cases with retrieval in this run; use a run made with --retrieval"
        )

    judge = LocalModel(
        model=args.judge_model,
        base_url=args.judge_url,
        api_key=os.environ.get("JUDGE_API_KEY", "EMPTY"),
    )
    metrics = build_metrics(judge)

    records: list[Row] = []
    for row in rows:
        record = score_case(row, references[row["id"]], metrics)
        records.append(record)
        scores = "  ".join(
            f"{n}={record[n]:.2f}" if record[n] is not None else f"{n}=error"
            for n in metrics
        )
        print(f"{row['id']}: {scores}", flush=True)

    out_path = args.run_dir / "deepeval.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print_summary(records)
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
