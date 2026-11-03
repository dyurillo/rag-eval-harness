# Eval dataset: Tallowmoth Systems internal docs

A synthetic RAG evaluation set: 12 internal documents for a fictional company and 48 questions about them.

## Provenance

The documents and questions were generated with Claude (an AI model) for this project. Tallowmoth Systems, Skerrow, its people, carriers, services and every policy and number are invented. Any resemblance to a real company or person is coincidental.

The corpus is fictional on purpose. A model can't have seen it during training, so the score without retrieval should be near zero, and the gap between the closed-book and open-book runs measures what retrieval actually adds.

Review status: A complete hand-review of every question and reference answer
has not been documented. `check_dataset.py` checks structural consistency,
not whether each reference answer is correct. Record a reviewer and date here
only after that review is completed.

## Contents

- `docs/`: 12 markdown files, about 3,000 words in total. Each file is split into chunks at `##` headings (80 chunks). A chunk's doc ID is its file name without `.md`.
- `rag_eval.jsonl`: 48 questions, one JSON object per line.
- `check_dataset.py`: consistency checks to run after editing anything here.

| Category | Count | Tag |
|---|---|---|
| Answerable from one doc | 38 | |
| Answerable only by combining two docs | 4 | `multi-doc` |
| Need a small inference, not just a lookup | 3 | `reasoning` |
| Worded differently from the source doc | 4 | `paraphrase` |
| Not answered by the docs | 6 | `unanswerable` |
| ...of which mention a closely related fact | 3 | `near-miss` |
| Scored with exact match | 30 | |

Topic tags: `product`, `oncall`, `incident`, `deploy`, `architecture`, `runbook`, `retention`, `access`, `expenses`, `pto`, `support`. Tags overlap, so counts don't sum to 48.

## Labeling rules

- `expected_doc_ids` lists the docs needed to answer. The docs avoid stating the same fact in two places, so for single-doc questions only one doc can answer, and retrieval labels stay unambiguous.
- `exact_answer` is the short phrase that must appear in a correct response. Both are normalized (lowercase, each punctuation character replaced with a space, whitespace collapsed) and the phrase must match on word boundaries. Answers that can't be pinned to one phrase have no exact answer and are scored by the judge only.
- For unanswerable questions, the correct response says the docs don't contain the answer. `reference_answer` explains what the docs do and don't say, for the judge.
- The `quote` scorer is diagnostic and never gates a case's pass/fail result. For answered, answerable cases it checks that the response carries exactly one `Quote: "<sentence>" [doc-id]` line whose text is a verbatim sentence from the retrieved chunks and whose doc id was retrieved; unanswerable cases and abstentions must carry no quote at all. It is listed in `scorers` on every row and is recorded as skipped when the run has no retrieval (that prompt asks for no quotes).

## Known limitations

- Exact match can still fail a correct answer that's phrased differently: `72-hour` doesn't match `72 hours`, `SEV-1` doesn't match `sev1`, and `2 million` doesn't match `2,000,000`. Treat the judge as the primary signal and exact-match failures as candidates for failure analysis.
- The corpus is small, so document-level retrieval is easy. A reference BM25 (tokens `[a-z0-9]+`, k1=1.5, b=0.75, idf `ln(1 + (N - df + 0.5) / (df + 0.5))`, each distinct query term counted once, zero-score chunks dropped, chunks at `##` headings) reaches hit@4 of 100%, hit@2 of 95% and hit@1 of 86%. Misses at low k are mostly the multi-doc questions. Comparisons of chunking or rerankers need a lower k or a larger corpus to show differences.
- The docs are cleaner and more consistent than real internal docs: no stale versions, contradictions or duplicated pages.
- 48 questions is a small sample. A difference of a few percentage points between two runs may be noise.
