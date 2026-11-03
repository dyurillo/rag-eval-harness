"""Tests for normalize() and exact_match()."""

import harness


def test_normalize_lowercases_replaces_punctuation_collapses_whitespace() -> None:
    assert harness.normalize("  The   Tag, v3! ") == "the tag v3"


def test_normalize_keeps_unicode_letters() -> None:
    assert harness.normalize("Caf\u00e9  \u00fcber") == "caf\u00e9 \u00fcber"


def test_exact_match_positive() -> None:
    assert harness.exact_match("90 seconds", "It sends a reading every 90 seconds, over LTE-M.")


def test_exact_match_ignores_punctuation() -> None:
    assert harness.exact_match("340", "The weekly stipend is $340 per week.")


def test_exact_match_number_not_inside_longer_number() -> None:
    # '8 hours' must not match inside '48 hours'
    assert not harness.exact_match("8 hours", "Tags can buffer up to 48 hours of readings.")
    assert harness.exact_match("8 hours", "Each grant lasts 8 hours.")


def test_exact_match_no_substring_inside_word() -> None:
    assert not harness.exact_match("340", "The budget is 3400 dollars.")
    assert not harness.exact_match("tag", "A retagging of the fleet was required.")


def test_exact_match_hyphen_becomes_space() -> None:
    # Punctuation is replaced with a space, so hyphenated and unhyphenated forms match.
    assert harness.exact_match("excursion-engine", "the excursion engine")
    assert harness.exact_match("excursion-engine", "The excursion-engine checks readings.")


def test_exact_match_punctuation_separates_tokens() -> None:
    assert harness.exact_match("340", "$340/week")
    assert harness.exact_match("85", "$85/day")
    assert harness.exact_match("400,000", "Fires when lag exceeds 400,000 messages.")


def test_exact_match_empty_answer_never_matches() -> None:
    assert not harness.exact_match("", "anything at all")