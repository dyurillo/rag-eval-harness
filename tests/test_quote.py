"""Tests for the diagnostic quote scorer (format compliance only, never gates)."""

import harness
from harness import Chunk, EvalCase

DOC = "oncall-policy"
CONTEXT = (
    "Hand off happens on Tuesdays at 10:00 Central. "
    "Rotations last 7 days. "
    "1. Skerrow Tags send readings over LTE-M through one of two cellular carriers."
)
CHUNKS: list[Chunk] = [Chunk(doc_id=DOC, text=CONTEXT)]


def case(answerable: bool = True) -> EvalCase:
    return EvalCase(
        id="q99",
        question="When does the on-call handoff happen?",
        answerable=answerable,
        reference_answer="Tuesdays at 10:00 Central",
        expected_doc_ids=[DOC],
    )


def test_skipped_without_retrieval() -> None:
    r = harness.score_quote(case(), "Tuesdays at 10:00 Central.", [], retrieval_on=False)
    assert (r.status, r.detail) == ("skipped", "retrieval disabled")


def test_no_quote_line_fails() -> None:
    r = harness.score_quote(case(), "Tuesdays at 10:00 Central.", CHUNKS, retrieval_on=True)
    assert r.status == "fail"
    assert r.detail == "no Quote: line"


def test_empty_quote_fails() -> None:
    answer = 'Tuesdays at 10:00 Central.\nQuote: "" [oncall-policy]'
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "fail"
    assert r.detail == "empty quote"


def test_one_word_fragment_fails() -> None:
    answer = 'Tuesdays at 10:00 Central.\nQuote: "Tuesday" [oncall-policy]'
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "fail"
    assert "whole sentence" in (r.detail or "")


def test_mid_sentence_fragment_fails() -> None:
    answer = 'Tuesdays at 10:00 Central.\nQuote: "at 10:00 Central" [oncall-policy]'
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "fail"
    assert "whole sentence" in (r.detail or "")


def test_whole_sentence_passes() -> None:
    answer = 'Tuesdays at 10:00 Central.\nQuote: "Hand off happens on Tuesdays at 10:00 Central." [oncall-policy]'
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "pass"


def test_numbered_list_item_is_a_whole_sentence() -> None:
    item = "1. Skerrow Tags send readings over LTE-M through one of two cellular carriers."
    answer = f"Tuesdays at 10:00 Central.\nQuote: \"{item}\" [oncall-policy]"
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "pass"


def test_curly_quotes_pass() -> None:
    answer = (
        "Tuesdays at 10:00 Central.\n"
        "Quote: \u201cHand off happens on Tuesdays at 10:00 Central.\u201d [oncall-policy]"
    )
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "pass"


def test_sentence_not_in_context_fails() -> None:
    answer = (
        "Tuesdays at 10:00 Central.\n"
        'Quote: "Hand off happens on Fridays at 9:00 Central." [oncall-policy]'
    )
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "fail"
    assert "whole sentence" in (r.detail or "")


def test_wrong_doc_id_fails() -> None:
    answer = (
        "Tuesdays at 10:00 Central.\n"
        'Quote: "Hand off happens on Tuesdays at 10:00 Central." [runbook-tag-offline]'
    )
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "fail"
    assert "not among retrieved" in (r.detail or "")


def test_two_quote_lines_fail() -> None:
    answer = (
        "Tuesdays at 10:00 Central.\n"
        'Quote: "Hand off happens on Tuesdays at 10:00 Central." [oncall-policy]\n'
        'Quote: "Rotations last 7 days." [oncall-policy]'
    )
    r = harness.score_quote(case(), answer, CHUNKS, retrieval_on=True)
    assert r.status == "fail"
    assert "2 Quote: lines" in (r.detail or "")


def test_unanswerable_with_quote_fails() -> None:
    answer = (
        "The context does not contain the answer.\n"
        'Quote: "Rotations last 7 days." [oncall-policy]'
    )
    r = harness.score_quote(case(answerable=False), answer, CHUNKS, retrieval_on=True)
    assert r.status == "fail"


def test_abstention_without_quote_passes() -> None:
    r = harness.score_quote(
        case(), "The context does not contain the answer.", CHUNKS, retrieval_on=True
    )
    assert (r.status, r.detail) == ("pass", "no quote (abstention)")


def test_looks_abstained() -> None:
    assert harness.looks_abstained("The context does not contain the answer.")
    assert harness.looks_abstained("I do not know.")
    assert not harness.looks_abstained("Tuesdays at 10:00 Central.")