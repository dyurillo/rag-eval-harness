"""Tests for chunking, BM25 ranking, and hit@k / recall@k."""

from pathlib import Path

import harness
from harness import Chunk


def _write(tmp_path: Path, name: str, text: str) -> None:
    (tmp_path / name).write_text(text, encoding="utf-8")


def test_tokenize() -> None:
    assert harness.tokenize("Hello, world! 42 tags.") == ["hello", "world", "42", "tags"]


def test_chunk_markdown_splits_at_headings() -> None:
    text = "# Title\n\nIntro paragraph.\n\n## Section A\n\ntext A\n\n## Section B\n\ntext B"
    assert harness.chunk_markdown(text) == [
        "# Title\n\nIntro paragraph.",
        "## Section A\n\ntext A",
        "## Section B\n\ntext B",
    ]


def test_chunk_markdown_no_headings_is_one_chunk() -> None:
    assert harness.chunk_markdown("just text\nmore") == ["just text\nmore"]


def test_chunk_markdown_starting_with_heading_has_no_intro_chunk() -> None:
    assert harness.chunk_markdown("## Only\nbody") == ["## Only\nbody"]


def test_load_corpus(tmp_path: Path) -> None:
    _write(tmp_path, "alpha.md", "Intro\n\n## S1\none\n\n## S2\ntwo")
    _write(tmp_path, "beta.md", "## Only\nthree")
    _write(tmp_path, "ignore.txt", "not markdown")
    chunks = harness.load_corpus(tmp_path)
    assert [(c.doc_id, c.text) for c in chunks] == [
        ("alpha", "Intro"),
        ("alpha", "## S1\none"),
        ("alpha", "## S2\ntwo"),
        ("beta", "## Only\nthree"),
    ]


def _tiny_corpus(tmp_path: Path) -> list[Chunk]:
    _write(tmp_path, "a.md", "## One\nalpha alpha beta")
    _write(tmp_path, "b.md", "## Two\nbeta gamma")
    _write(tmp_path, "c.md", "## Three\ngamma delta delta")
    return harness.load_corpus(tmp_path)


def test_bm25_ranks_most_relevant_first(tmp_path: Path) -> None:
    # Hand-computed Okapi BM25 (k1=1.5, b=0.75, non-negative idf) gives
    # a ~ 1.69 > b ~ 0.51 > c = 0 for query "alpha beta". Chunk c scores
    # zero (no shared term) and is dropped by rank_chunks.
    chunks = _tiny_corpus(tmp_path)
    ranked = harness.rank_chunks("alpha beta", chunks, k=3)
    assert [c.doc_id for c in ranked] == ["a", "b"]


def test_rank_chunks_top_k(tmp_path: Path) -> None:
    chunks = _tiny_corpus(tmp_path)
    assert [c.doc_id for c in harness.rank_chunks("alpha beta", chunks, k=1)] == ["a"]


def test_rank_chunks_no_matching_terms_returns_empty(tmp_path: Path) -> None:
    chunks = _tiny_corpus(tmp_path)
    assert harness.rank_chunks("zeta", chunks, k=4) == []


def test_doc_ids_of_unique_and_ordered() -> None:
    chunks = [Chunk("a", "x"), Chunk("b", "y"), Chunk("a", "z")]
    assert harness.doc_ids_of(chunks) == ["a", "b"]


def test_hit_at_k() -> None:
    assert harness.hit_at_k({"a", "b"}, {"b", "c"}) == 1
    assert harness.hit_at_k({"a", "b"}, {"c"}) == 0


def test_two_expected_docs_only_one_retrieved() -> None:
    assert harness.hit_at_k({"a", "b"}, {"a"}) == 1
    assert harness.recall_at_k({"a", "b"}, {"a"}) == 0.5


def test_recall_at_k_full_and_empty() -> None:
    assert harness.recall_at_k({"a"}, {"a", "b"}) == 1.0
    assert harness.recall_at_k(set(), {"a"}) == 0.0


def test_score_retrieval_pass_and_fail() -> None:
    case = harness.EvalCase(
        id="q1",
        question="q",
        answerable=True,
        expected_doc_ids=["a", "b"],
        scorers=["retrieval"],
    )
    ok = harness.score_retrieval(case, [Chunk("b", "x")], k=2, retrieval_on=True)
    assert ok.status == "pass"  # hit@2 = 1
    assert ok.score == 0.5  # recall@2
    bad = harness.score_retrieval(case, [Chunk("c", "y")], k=2, retrieval_on=True)
    assert bad.status == "fail"
    assert bad.score == 0.0


def test_score_retrieval_skipped_when_retrieval_off() -> None:
    case = harness.EvalCase(
        id="q1", question="q", answerable=True, expected_doc_ids=["a"], scorers=["retrieval"]
    )
    result = harness.score_retrieval(case, [Chunk("a", "x")], k=4, retrieval_on=False)
    assert result.status == "skipped"