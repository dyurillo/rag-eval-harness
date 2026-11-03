"""Tests for report generation from a fixture run directory."""

import json
from pathlib import Path

import pytest

import report


def _case(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "c1",
        "question": "How often does the tag report?",
        "answerable": True,
        "tags": ["product"],
        "expected_doc_ids": ["d1"],
        "retrieved_doc_ids": ["d1"],
        "answer": "Every 90 seconds.",
        "error": None,
        "latency_ms": 100.0,
        "prompt_tokens": 10,
        "completion_tokens": 5,
        "cost_usd": 0.0,
        "scorers": [
            {"name": "exact", "status": "pass"},
            {"name": "judge", "status": "pass", "score": 5, "detail": "agrees"},
            {"name": "retrieval", "status": "pass", "score": 1.0, "detail": "hit@2=1, recall@2=1.00"},
        ],
        "passed": True,
    }
    base.update(overrides)
    return base


def _make_run(tmp_path: Path) -> Path:
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    meta = {
        "model": "test-model",
        "judge_model": "judge-model",
        "retrieval": True,
        "k": 2,
        "dataset": "datasets/rag_eval.jsonl",
        "dataset_sha256": "abc123",
        "judge_threshold": 4,
        "start_time": "2026-01-01T00:00:00+00:00",
        "end_time": "2026-01-01T00:01:00+00:00",
    }
    (run_dir / "run.json").write_text(json.dumps(meta), encoding="utf-8")
    cases = [
        _case(),
        _case(
            id="c2",
            question="When does the handoff happen?",
            tags=["product"],
            expected_doc_ids=["d1", "d2"],
            retrieved_doc_ids=["d2"],
            answer="Mondays.",
            latency_ms=300.0,
            prompt_tokens=20,
            completion_tokens=8,
            scorers=[
                {"name": "exact", "status": "fail"},
                {"name": "judge", "status": "fail", "score": 2, "detail": "wrong day"},
                {"name": "retrieval", "status": "fail", "score": 0.5, "detail": "hit@2=1, recall@2=0.50"},
            ],
            passed=False,
        ),
        _case(
            id="c3",
            question="What is the 401(k) match?",
            answerable=False,
            tags=["unanswerable"],
            expected_doc_ids=[],
            retrieved_doc_ids=[],
            answer="The docs don't say. Actually, I think it is 6%.",
            latency_ms=50.0,
            prompt_tokens=12,
            completion_tokens=3,
            scorers=[{"name": "judge", "status": "fail", "score": 1, "detail": "invents a number"}],
            passed=False,
        ),
        _case(
            id="c4",
            question="Who approves hotfixes?",
            tags=["oncall"],
            expected_doc_ids=["d3"],
            retrieved_doc_ids=[],
            answer=None,
            error="model request failed: boom",
            latency_ms=None,
            prompt_tokens=0,
            completion_tokens=0,
            scorers=[],
            passed=False,
        ),
    ]
    with (run_dir / "results.jsonl").open("w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps(c) + "\n")
    return run_dir


def test_summary_values(tmp_path: Path) -> None:
    data = report.build_report_data(_make_run(tmp_path))
    s = data["summary"]
    assert s["total"] == 4
    assert s["passed"] == 1
    assert s["pass_rate"] == 0.25
    assert s["scorer_rates"]["exact"] == {"passed": 1, "ran": 2}
    assert s["scorer_rates"]["judge"] == {"passed": 1, "ran": 3}
    assert s["scorer_rates"]["retrieval"] == {"passed": 1, "ran": 2}
    assert s["tag_rates"]["product"] == {"passed": 1, "ran": 2}
    assert s["tag_rates"]["unanswerable"] == {"passed": 0, "ran": 1}
    assert s["tag_rates"]["oncall"] == {"passed": 0, "ran": 1}
    assert s["mean_judge_score"] == pytest.approx(2 + 2 / 3)  # (5 + 2 + 1) / 3
    assert s["hallucination"] == {"num": 1, "den": 1, "rate": 1.0}
    assert s["retrieval_hit"] == 1.0  # both retrieval cases hit
    assert s["retrieval_recall"] == pytest.approx(0.75)  # (1.0 + 0.5) / 2
    assert s["latency_p50_ms"] == 100.0  # nearest-rank over [50, 100, 300]
    assert s["latency_p95_ms"] == 300.0
    assert s["prompt_tokens"] == 42
    assert s["completion_tokens"] == 16
    assert s["total_tokens"] == 58
    assert s["total_cost_usd"] == 0.0
    assert s["errors"] == 1
    # Header fields come from run.json.
    assert data["model"] == "test-model"
    assert data["judge_model"] == "judge-model"
    assert data["retrieval"] is True
    assert data["k"] == 2


def test_reports_written_and_self_contained(tmp_path: Path) -> None:
    run_dir = _make_run(tmp_path)
    md_path, html_path = report.write_reports(run_dir)
    assert md_path.name == "report.md"
    assert html_path.name == "report.html"
    md_text = md_path.read_text(encoding="utf-8")
    html_text = html_path.read_text(encoding="utf-8")
    for needle in ("test-model", "judge-model", "c1", "c2", "c3", "c4", "25.0%"):
        assert needle in md_text, needle
        assert needle in html_text, needle
    assert "on (k=2)" in md_text
    # The failed case's response and judge reason appear in the failures section.
    assert "Mondays." in md_text
    assert "Mondays." in html_text
    assert "wrong day" in html_text
    # HTML must be self-contained: inline CSS, no JS, no external assets.
    assert "<style>" in html_text
    assert "<script" not in html_text.lower()
    assert "http" not in html_text


def test_summary_without_retrieval(tmp_path: Path) -> None:
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    (run_dir / "run.json").write_text(
        json.dumps(
            {
                "model": "m",
                "judge_model": "j",
                "retrieval": False,
                "k": 0,
                "dataset": "d.jsonl",
                "dataset_sha256": "x",
                "judge_threshold": 4,
                "start_time": "2026-01-01T00:00:00+00:00",
                "end_time": "2026-01-01T00:00:10+00:00",
            }
        ),
        encoding="utf-8",
    )
    case = {
        "id": "c1",
        "question": "q",
        "answerable": True,
        "tags": [],
        "expected_doc_ids": [],
        "retrieved_doc_ids": [],
        "answer": "a",
        "error": None,
        "latency_ms": 10.0,
        "prompt_tokens": 1,
        "completion_tokens": 2,
        "cost_usd": 0.0,
        "scorers": [
            {"name": "judge", "status": "pass", "score": 5, "detail": "ok"},
            {"name": "retrieval", "status": "skipped", "detail": "retrieval disabled"},
        ],
        "passed": True,
    }
    (run_dir / "results.jsonl").write_text(json.dumps(case) + "\n", encoding="utf-8")
    s = report.build_report_data(run_dir)["summary"]
    assert s["retrieval_hit"] is None
    assert s["retrieval_recall"] is None
    assert s["latency_p50_ms"] == 10.0
    assert s["pass_rate"] == 1.0


def test_missing_run_dir_raises(tmp_path: Path) -> None:
    with pytest.raises(report.ReportError):
        report.build_report_data(tmp_path / "does-not-exist")