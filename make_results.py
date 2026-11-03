"""Build the committed results/ tree from the raw run directories in runs/.

For each cell of the README's results table, copies `run.json`,
`results.jsonl` and `deepeval.jsonl` (when present) from
`runs/<timestamp>/` into `results/<cell>/`, then renders `report.md` /
`report.html` there via `report.write_reports`.

Usage:
    uv run python make_results.py
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import report

# README results-table cell -> run directory (final batch, 2026-10-23).
RUNS: dict[str, str] = {
    "base-no-retrieval": "20261023T193448Z",
    "base-k1": "20261023T193527Z",
    "base-k2": "20261023T193608Z",
    "base-k4": "20261023T193650Z",
    "adapter-no-retrieval": "20261023T193731Z",
    "adapter-k1": "20261023T193810Z",
    "adapter-k2": "20261023T193853Z",
    "adapter-k4": "20261023T193929Z",
}

FILES = ("run.json", "results.jsonl", "deepeval.jsonl")


def build(results_root: Path) -> int:
    """Copy each run into results/<cell>/ and render its reports."""
    for cell, ts in RUNS.items():
        src = Path("runs") / ts
        if not (src / "run.json").is_file():
            print(f"error: missing {src / 'run.json'} (cell {cell!r})", file=sys.stderr)
            return 1
        dst = results_root / cell
        dst.mkdir(parents=True, exist_ok=True)
        for name in FILES:
            p = src / name
            if p.is_file():
                shutil.copy2(p, dst / name)
        md_path, html_path = report.write_reports(dst)
        print(f"{cell}: {ts} -> {dst} ({md_path.name}, {html_path.name})")
    return 0


def main() -> int:
    return build(Path("results"))


if __name__ == "__main__":
    sys.exit(main())
