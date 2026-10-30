"""Write report.md and report.html for a harness run directory.

Usage:
    uv run report.py runs/<timestamp>

The HTML report is rendered from a single Jinja2 template defined as a string
below; it is self-contained (inline CSS, no JS, no external assets).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from jinja2 import Environment
from pydantic import ValidationError

from harness import CaseResult, ScorerResult, hit_at_k, looks_abstained, recall_at_k

_HTML_ENV = Environment(autoescape=True)


class ReportError(Exception):
    """Raised when a run directory cannot be read or validated."""


# ---------------------------------------------------------------------------
# Loading (I/O edge)
# ---------------------------------------------------------------------------


def load_run(run_dir: Path) -> tuple[dict[str, Any], list[CaseResult]]:
    """Read run.json and results.jsonl from run_dir."""
    meta_path = run_dir / "run.json"
    results_path = run_dir / "results.jsonl"
    for p in (meta_path, results_path):
        if not p.is_file():
            raise ReportError(f"missing {p}")
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ReportError(f"invalid {meta_path}: {exc}") from exc
    if not isinstance(meta, dict):
        raise ReportError(f"invalid {meta_path}: top-level JSON must be an object")
    cases: list[CaseResult] = []
    text = results_path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            cases.append(CaseResult.model_validate(json.loads(line)))
        except (json.JSONDecodeError, ValidationError) as exc:
            raise ReportError(f"{results_path} line {lineno}: {exc}") from exc
    return meta, cases


# ---------------------------------------------------------------------------
# Summary statistics (pure)
# ---------------------------------------------------------------------------


def percentile(values: Sequence[float], q: float) -> float | None:
    """Nearest-rank percentile (q in (0, 1]) of a possibly-unsorted list."""
    if not values:
        return None
    ordered = sorted(values)
    rank = max(1, math.ceil(q * len(ordered)))
    return ordered[rank - 1]


def _pct(x: float) -> str:
    return f"{x * 100:.1f}%"


def compute_summary(cases: Sequence[CaseResult]) -> dict[str, Any]:
    total = len(cases)
    passed = sum(1 for c in cases if c.passed)

    scorer_rates: dict[str, dict[str, int]] = {}
    tag_rates: dict[str, dict[str, int]] = {}
    for c in cases:
        for r in c.scorers:
            if r.status == "skipped":
                continue
            entry = scorer_rates.setdefault(r.name, {"passed": 0, "ran": 0})
            entry["ran"] += 1
            if r.status == "pass":
                entry["passed"] += 1
        for tag in c.tags:
            entry = tag_rates.setdefault(tag, {"passed": 0, "ran": 0})
            entry["ran"] += 1
            if c.passed:
                entry["passed"] += 1

    judge_scores = [r.score for c in cases for r in c.scorers if r.name == "judge" and r.score is not None]
    mean_judge = sum(judge_scores) / len(judge_scores) if judge_scores else None

    # Hallucination: unanswerable cases whose judge score is 2 or lower.
    halluc_num = 0
    halluc_den = 0
    for c in cases:
        if c.answerable:
            continue
        for r in c.scorers:
            if r.name == "judge" and r.score is not None:
                halluc_den += 1
                if r.score <= 2:
                    halluc_num += 1

    hits: list[float] = []
    recalls: list[float] = []
    for c in cases:
        if any(r.name == "retrieval" and r.status != "skipped" for r in c.scorers):
            want = set(c.expected_doc_ids)
            got = set(c.retrieved_doc_ids)
            hits.append(float(hit_at_k(want, got)))
            recalls.append(recall_at_k(want, got))

    # Quote compliance over answered questions only: answerable cases whose
    # response does not abstain (excludes unanswerables and abstentions).
    answered = [
        c
        for c in cases
        if c.answerable and c.answer is not None and not looks_abstained(c.answer)
    ]
    quote_answered = {
        "num": sum(
            1 for c in answered if any(r.name == "quote" and r.status == "pass" for r in c.scorers)
        ),
        "den": len(answered),
    }

    latencies = [c.latency_ms for c in cases if c.latency_ms is not None]
    prompt_tokens = sum(c.prompt_tokens or 0 for c in cases)
    completion_tokens = sum(c.completion_tokens or 0 for c in cases)

    return {
        "total": total,
        "passed": passed,
        "pass_rate": passed / total if total else 0.0,
        "scorer_rates": scorer_rates,
        "tag_rates": tag_rates,
        "mean_judge_score": mean_judge,
        "hallucination": {
            "num": halluc_num,
            "den": halluc_den,
            "rate": halluc_num / halluc_den if halluc_den else None,
        },
        "retrieval_hit": sum(hits) / len(hits) if hits else None,
        "retrieval_recall": sum(recalls) / len(recalls) if recalls else None,
        "quote_answered": quote_answered,
        "latency_p50_ms": percentile(latencies, 0.50),
        "latency_p95_ms": percentile(latencies, 0.95),
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "total_cost_usd": sum(c.cost_usd for c in cases),
        "errors": sum(1 for c in cases if c.error is not None),
    }


# ---------------------------------------------------------------------------
# Table rows (pure)
# ---------------------------------------------------------------------------


def _mark(result: ScorerResult | None) -> tuple[str, str]:
    """(label, css class) for a scorer cell."""
    if result is None:
        return "n/a", "na"
    if result.status == "skipped":
        return "skip", "skip"
    return result.status, result.status


def case_rows(cases: Sequence[CaseResult]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for c in cases:
        by_name: dict[str, ScorerResult] = {}
        for r in c.scorers:
            by_name[r.name] = r
        judge = by_name.get("judge")
        exact_label, exact_cls = _mark(by_name.get("exact"))
        judge_label, judge_cls = _mark(judge)
        ret_label, ret_cls = _mark(by_name.get("retrieval"))
        quote_label, quote_cls = _mark(by_name.get("quote"))
        if c.error is not None:
            result_label, result_cls = "error", "na"
        elif c.passed:
            result_label, result_cls = "pass", "pass"
        else:
            result_label, result_cls = "fail", "fail"
        rows.append(
            {
                "id": c.id,
                "result": result_label,
                "result_cls": result_cls,
                "exact": exact_label,
                "exact_cls": exact_cls,
                "judge": judge_label,
                "judge_cls": judge_cls,
                "retrieval": ret_label,
                "retrieval_cls": ret_cls,
                "quote": quote_label,
                "quote_cls": quote_cls,
                "judge_score": str(judge.score) if judge is not None and judge.score is not None else "n/a",
                "judge_reason": (judge.detail if judge is not None and judge.detail else c.error) or "n/a",
                "latency_ms": f"{c.latency_ms:.0f}" if c.latency_ms is not None else "n/a",
                "cost_usd": f"{c.cost_usd:.6f}",
            }
        )
    return rows


def failure_rows(cases: Sequence[CaseResult]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for c in cases:
        if c.passed:
            continue
        judge = next((r for r in c.scorers if r.name == "judge"), None)
        out.append(
            {
                "id": c.id,
                "question": c.question,
                "response": c.answer
                if c.answer is not None
                else (f"(model call failed: {c.error})" if c.error else "(no response)"),
                "retrieved_doc_ids": c.retrieved_doc_ids,
                "judge": (
                    f"score {judge.score} - {judge.detail}"
                    if judge is not None and judge.detail is not None
                    else "n/a"
                ),
                "failed_scorers": [r.name for r in c.scorers if r.status == "fail"],
            }
        )
    return out


# ---------------------------------------------------------------------------
# Report assembly
# ---------------------------------------------------------------------------


def summary_items(data: dict[str, Any]) -> list[tuple[str, str]]:
    s: dict[str, Any] = data["summary"]
    items: list[tuple[str, str]] = []
    items.append(("Cases", f"{s['passed']}/{s['total']}"))
    items.append(("Overall pass rate", _pct(s["pass_rate"])))
    for name in ("exact", "judge", "retrieval", "quote"):
        entry = s["scorer_rates"].get(name)
        if entry and entry["ran"]:
            items.append(
                (f"Pass rate ({name})", f"{entry['passed']}/{entry['ran']} = {_pct(entry['passed'] / entry['ran'])}")
            )
        else:
            items.append((f"Pass rate ({name})", "n/a (not run)"))
    qa: dict[str, int] = s.get("quote_answered", {})
    if qa.get("den") and s["scorer_rates"].get("quote", {}).get("ran"):
        items.append(
            (
                "Quote compliance (answered questions only)",
                f"{qa['num']}/{qa['den']} = {_pct(qa['num'] / qa['den'])}",
            )
        )
    for tag in sorted(s["tag_rates"]):
        entry = s["tag_rates"][tag]
        items.append(
            (f"Pass rate (tag: {tag})", f"{entry['passed']}/{entry['ran']} = {_pct(entry['passed'] / entry['ran'])}")
        )
    mean_judge = s["mean_judge_score"]
    items.append(("Mean judge score", f"{mean_judge:.2f}" if mean_judge is not None else "n/a"))
    h: dict[str, Any] = s["hallucination"]
    items.append(
        (
            "Hallucination rate (unanswerable, judge score <= 2)",
            f"{h['num']}/{h['den']} = {_pct(h['rate'])}" if h["den"] else "n/a",
        )
    )
    if s["retrieval_hit"] is not None:
        items.append((f"Retrieval hit@{data['k']}", _pct(s["retrieval_hit"])))
        items.append((f"Retrieval recall@{data['k']}", _pct(s["retrieval_recall"])))
    p50 = s["latency_p50_ms"]
    items.append(("Latency p50", f"{p50:.0f} ms" if p50 is not None else "n/a"))
    p95 = s["latency_p95_ms"]
    items.append(("Latency p95", f"{p95:.0f} ms" if p95 is not None else "n/a"))
    items.append(
        ("Total tokens", f"{s['total_tokens']} (prompt {s['prompt_tokens']}, completion {s['completion_tokens']})")
    )
    items.append(("Total cost", f"${s['total_cost_usd']:.4f}"))
    items.append(("Errors", str(s["errors"])))
    return items


def build_report_data(run_dir: Path) -> dict[str, Any]:
    meta, cases = load_run(run_dir)
    data: dict[str, Any] = {
        "model": meta.get("model", "?"),
        "judge_model": meta.get("judge_model", "?"),
        "retrieval": bool(meta.get("retrieval", False)),
        "k": int(meta.get("k", 0)),
        "dataset": meta.get("dataset", "?"),
        "dataset_sha256": meta.get("dataset_sha256", "?"),
        "start_time": meta.get("start_time", "?"),
        "end_time": meta.get("end_time", "?"),
        "judge_threshold": meta.get("judge_threshold", "?"),
        "summary": compute_summary(cases),
        "rows": case_rows(cases),
        "failures": failure_rows(cases),
    }
    data["summary_items"] = summary_items(data)
    return data


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Eval run report</title>
<style>
body { font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
       margin: 2rem auto; max-width: 64rem; padding: 0 1rem; color: #1a1a1a; line-height: 1.45; }
h1 { font-size: 1.5rem; }
h2 { font-size: 1.2rem; margin-top: 2rem; border-bottom: 1px solid #ddd; padding-bottom: .3rem; }
table { border-collapse: collapse; width: 100%; margin: .75rem 0; font-size: .9rem; }
th, td { border: 1px solid #ccc; padding: .35rem .5rem; text-align: left; vertical-align: top; }
th { background: #f4f4f4; }
.meta td:first-child { font-weight: 600; width: 14rem; }
.pass { color: #1a7f37; font-weight: 600; }
.fail { color: #cf222e; font-weight: 600; }
.skip, .na { color: #6e7781; }
pre { white-space: pre-wrap; word-wrap: break-word; background: #f6f8fa;
     padding: .6rem; border-radius: 6px; }
.failure { margin: 1rem 0; padding: .75rem 1rem; border: 1px solid #e5534b33;
          border-left: 4px solid #cf222e; border-radius: 4px; }
.failure h3 { margin: 0 0 .5rem; font-size: 1rem; }
.label { font-weight: 600; }
</style>
</head>
<body>
<h1>Eval run report</h1>
<table class="meta">
<tr><td>Model</td><td>{{ model }}</td></tr>
<tr><td>Judge</td><td>{{ judge_model }} (threshold {{ judge_threshold }})</td></tr>
<tr><td>Retrieval</td><td>{{ "on" if retrieval else "off" }}{% if retrieval %} (k={{ k }}){% endif %}</td></tr>
<tr><td>Dataset</td><td>{{ dataset }} (sha256 {{ dataset_sha256 }})</td></tr>
<tr><td>Started / ended (UTC)</td><td>{{ start_time }} / {{ end_time }}</td></tr>
</table>

<h2>Summary</h2>
<table>
<tr><th>Metric</th><th>Value</th></tr>
{% for label, value in summary_items %}
<tr><td>{{ label }}</td><td>{{ value }}</td></tr>
{% endfor %}
</table>

<h2>Per-question results</h2>
<table>
<tr><th>id</th><th>result</th><th>exact</th><th>judge</th><th>retrieval</th><th>quote</th>
<th>judge score</th><th>judge reason</th><th>latency (ms)</th><th>cost (USD)</th></tr>
{% for row in rows %}
<tr>
<td>{{ row.id }}</td>
<td class="{{ row.result_cls }}">{{ row.result }}</td>
<td class="{{ row.exact_cls }}">{{ row.exact }}</td>
<td class="{{ row.judge_cls }}">{{ row.judge }}</td>
<td class="{{ row.retrieval_cls }}">{{ row.retrieval }}</td>
<td class="{{ row.quote_cls }}">{{ row.quote }}</td>
<td>{{ row.judge_score }}</td>
<td>{{ row.judge_reason }}</td>
<td>{{ row.latency_ms }}</td>
<td>{{ row.cost_usd }}</td>
</tr>
{% endfor %}
</table>

<h2>Failures</h2>
{% if failures %}
{% for f in failures %}
<div class="failure">
<h3>{{ f.id }}</h3>
<p><span class="label">Question:</span> {{ f.question }}</p>
<p><span class="label">Response:</span></p>
<pre>{{ f.response }}</pre>
<p><span class="label">Retrieved docs:</span> {{ f.retrieved_doc_ids | join(", ") or "(none)" }}</p>
<p><span class="label">Judge:</span> {{ f.judge }}</p>
<p><span class="label">Failed scorers:</span> {{ f.failed_scorers | join(", ") or "(model call error)" }}</p>
</div>
{% endfor %}
{% else %}
<p>No failures.</p>
{% endif %}
</body>
</html>
"""


def render_html(data: dict[str, Any]) -> str:
    return _HTML_ENV.from_string(HTML_TEMPLATE).render(**data)


def _md_cell(text: str, limit: int = 120) -> str:
    text = " ".join(text.split()).replace("|", "\\|")
    if len(text) > limit:
        text = text[: limit - 3] + "..."
    return text


def render_markdown(data: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Eval run report")
    lines.append("")
    lines.append(f"- Model: {data['model']}")
    lines.append(f"- Judge: {data['judge_model']} (threshold {data['judge_threshold']})")
    retrieval = f"on (k={data['k']})" if data["retrieval"] else "off"
    lines.append(f"- Retrieval: {retrieval}")
    lines.append(f"- Dataset: {data['dataset']} (sha256 {data['dataset_sha256']})")
    lines.append(f"- Start / end (UTC): {data['start_time']} / {data['end_time']}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    for label, value in data["summary_items"]:
        lines.append(f"| {label} | {value} |")
    lines.append("")
    lines.append("## Per-question results")
    lines.append("")
    lines.append(
        "| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |"
    )
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for row in data["rows"]:
        lines.append(
            f"| {row['id']} | {row['result']} | {row['exact']} | {row['judge']}"
            f" | {row['retrieval']} | {row['quote']} | {row['judge_score']} | {_md_cell(row['judge_reason'])}"
            f" | {row['latency_ms']} | {row['cost_usd']} |"
        )
    lines.append("")
    lines.append("## Failures")
    lines.append("")
    if not data["failures"]:
        lines.append("No failures.")
        lines.append("")
    for f in data["failures"]:
        failed = ", ".join(f["failed_scorers"]) or "model call error"
        lines.append(f"### {f['id']} - {failed}")
        lines.append("")
        lines.append(f"**Question:** {f['question']}")
        lines.append("")
        lines.append("**Response:**")
        lines.append("")
        for resp_line in f["response"].splitlines():
            lines.append(f"    {resp_line}")
        lines.append("")
        lines.append(f"**Retrieved docs:** {', '.join(f['retrieved_doc_ids']) or '(none)'}")
        lines.append("")
        lines.append(f"**Judge:** {f['judge']}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def write_reports(run_dir: Path) -> tuple[Path, Path]:
    """Build the report and write report.md / report.html into run_dir."""
    data = build_report_data(run_dir)
    md_path = run_dir / "report.md"
    html_path = run_dir / "report.html"
    md_path.write_text(render_markdown(data), encoding="utf-8")
    html_path.write_text(render_html(data), encoding="utf-8")
    return md_path, html_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Write report.md and report.html for a harness run directory."
    )
    parser.add_argument("run_dir", help="run directory, e.g. runs/20260101T000000Z")
    args = parser.parse_args(argv)
    run_dir = Path(args.run_dir)
    try:
        md_path, html_path = write_reports(run_dir)
    except (OSError, ReportError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {md_path}")
    print(f"wrote {html_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())