# results/

This directory holds the eight runs behind the [README](../README.md)'s
results table. Each folder has per-case outputs, run metadata, and Markdown
and HTML reports; the k = 1 folders also have DeepEval scores. Run
`uv run python make_results.py` from the repository root to regenerate them
from local `runs/` outputs.

| folder | model | retrieval | k | README table cell | passed |
|---|---|---|---:|---|---:|
| `base-no-retrieval/` | `google/gemma-3-1b-it` | off | — | base, no retrieval | 7/48 |
| `base-k1/` | `google/gemma-3-1b-it` | on | 1 | base, k = 1 | 25/48 |
| `base-k2/` | `google/gemma-3-1b-it` | on | 2 | base, k = 2 | 28/48 |
| `base-k4/` | `google/gemma-3-1b-it` | on | 4 | base, k = 4 | 30/48 |
| `adapter-no-retrieval/` | `rag-lora-1b` | off | — | adapter, no retrieval | 6/48 |
| `adapter-k1/` | `rag-lora-1b` | on | 1 | adapter, k = 1 | 26/48 |
| `adapter-k2/` | `rag-lora-1b` | on | 2 | adapter, k = 2 | 25/48 |
| `adapter-k4/` | `rag-lora-1b` | on | 4 | adapter, k = 4 | 27/48 |

The DeepEval figures aggregate k = 1 comparisons: 36/42 base agreement,
38/42 adapter agreement, and 74/84 (88%) combined, from
[base-k1/deepeval.jsonl](base-k1/deepeval.jsonl) and
[adapter-k1/deepeval.jsonl](adapter-k1/deepeval.jsonl).
