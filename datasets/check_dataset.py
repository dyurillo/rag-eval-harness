"""Consistency checks for rag_eval.jsonl against the docs in datasets/docs.

Run after editing questions or docs:  uv run datasets/check_dataset.py
Exits non-zero if any check fails. Warnings don't fail the run.
"""

import json
import re
import string
import sys
from pathlib import Path
from typing import cast

HERE = Path(__file__).parent
DATASET = HERE / "rag_eval.jsonl"
DOCS_DIR = HERE / "docs"

REQUIRED: dict[str, type | tuple[type, ...]] = {
    "id": str,
    "question": str,
    "reference_answer": (str, type(None)),
    "exact_answer": (str, type(None)),
    "expected_doc_ids": list,
    "scorers": list,
    "tags": list,
    "answerable": bool,
}
VALID_SCORERS = {"exact", "judge", "retrieval", "quote"}
PUNCT = str.maketrans(string.punctuation, " " * len(string.punctuation))


def normalize(text: str) -> str:
    """Lowercase, replace punctuation with spaces, collapse whitespace.

    Matches the harness's exact-match normalization.
    """
    return re.sub(r"\s+", " ", text.lower().translate(PUNCT)).strip()


def contains_phrase(phrase: str, text: str) -> bool:
    """True if phrase appears in text on word boundaries (both normalized)."""
    return re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text) is not None


def check_row(
    row: dict[str, object], docs: dict[str, str]
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for field, kind in REQUIRED.items():
        if field not in row:
            errors.append(f"missing field {field!r}")
        elif not isinstance(row[field], kind):
            errors.append(f"field {field!r} has the wrong type")
    if errors:
        return errors, warnings

    # Types were checked above.
    scorers = set(cast(list[str], row["scorers"]))
    expected = cast(list[str], row["expected_doc_ids"])
    exact = row["exact_answer"]
    answerable = row["answerable"]

    if bad := scorers - VALID_SCORERS:
        errors.append(f"unknown scorers {sorted(bad)}")
    if ("exact" in scorers) != (exact is not None):
        errors.append("'exact' scorer and exact_answer must be set together")

    if answerable:
        if not expected:
            errors.append("answerable row has no expected_doc_ids")
        if "retrieval" not in scorers:
            warnings.append("answerable row isn't scored on retrieval")
        if missing := [d for d in expected if d not in docs]:
            errors.append(f"expected docs not found: {missing}")
    else:
        if expected or exact is not None or "retrieval" in scorers:
            errors.append("unanswerable rows take no docs, exact answer or retrieval")

    if isinstance(exact, str) and not errors:
        target = normalize(exact)
        if not any(contains_phrase(target, docs[d]) for d in expected):
            errors.append(f"exact answer {exact!r} not found in {expected}")
        ref = row["reference_answer"]
        if isinstance(ref, str) and not contains_phrase(target, normalize(ref)):
            errors.append(f"exact answer {exact!r} not in reference_answer")
        elsewhere = [
            d
            for d, text in docs.items()
            if d not in expected and contains_phrase(target, text)
        ]
        if elsewhere:
            warnings.append(f"exact answer {exact!r} also appears in {elsewhere}")

    return errors, warnings


def main() -> int:
    docs = {p.stem: normalize(p.read_text()) for p in sorted(DOCS_DIR.glob("*.md"))}
    seen: set[str] = set()
    n_errors = 0
    n_rows = 0

    for lineno, line in enumerate(DATASET.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        n_rows += 1
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            print(f"line {lineno}: invalid JSON: {exc}")
            n_errors += 1
            continue

        errors, warnings = check_row(row, docs)
        row_id = row.get("id", f"line {lineno}")
        if row_id in seen:
            errors.append("duplicate id")
        seen.add(row_id)

        for msg in errors:
            print(f"ERROR {row_id}: {msg}")
        for msg in warnings:
            print(f"warn  {row_id}: {msg}")
        n_errors += len(errors)

    print(f"{n_rows} rows, {len(docs)} docs, {n_errors} errors")
    return 1 if n_errors else 0


if __name__ == "__main__":
    sys.exit(main())
