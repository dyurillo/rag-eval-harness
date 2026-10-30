"""Tests for dataset loading and validation."""

from pathlib import Path

import pytest

from harness import DatasetError, load_dataset

REPO_ROOT = Path(__file__).resolve().parent.parent

VALID = (
    '{"id": "q1", "question": "Q?", "answerable": true, "reference_answer": null,'
    ' "exact_answer": null, "expected_doc_ids": [], "scorers": ["judge"], "tags": []}'
)


def _write_dataset(tmp_path: Path, lines: list[str]) -> Path:
    path = tmp_path / "ds.jsonl"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def test_load_valid_row(tmp_path: Path) -> None:
    cases = load_dataset(_write_dataset(tmp_path, [VALID]))
    assert len(cases) == 1
    assert cases[0].id == "q1"
    assert cases[0].scorers == ["judge"]


def test_blank_lines_are_ignored(tmp_path: Path) -> None:
    cases = load_dataset(_write_dataset(tmp_path, ["", VALID, ""]))
    assert len(cases) == 1


def test_bad_json_reports_line_number(tmp_path: Path) -> None:
    path = _write_dataset(tmp_path, [VALID, "{not json"])
    with pytest.raises(DatasetError, match="line 2"):
        load_dataset(path)


def test_missing_required_field_reports_line_number(tmp_path: Path) -> None:
    bad = '{"id": "q2", "scorers": ["judge"], "answerable": true}'  # no question
    path = _write_dataset(tmp_path, [VALID, bad])
    with pytest.raises(DatasetError, match="line 2"):
        load_dataset(path)


def test_invalid_scorer_name_reports_line_number(tmp_path: Path) -> None:
    bad = '{"id": "q3", "question": "Q", "scorers": ["exacto"], "answerable": true}'
    path = _write_dataset(tmp_path, [bad])
    with pytest.raises(DatasetError, match="line 1"):
        load_dataset(path)


def test_real_dataset_loads_without_errors() -> None:
    path = REPO_ROOT / "datasets" / "rag_eval.jsonl"
    cases = load_dataset(path)
    assert len(cases) == 48
    assert {c.id for c in cases} == {f"q{i:02d}" for i in range(1, 49)}
    assert sum(1 for c in cases if not c.answerable) == 6
    assert all(c.scorers for c in cases)
    # Every case that uses the exact scorer has an exact_answer to check.
    assert all(c.exact_answer is not None for c in cases if "exact" in c.scorers)