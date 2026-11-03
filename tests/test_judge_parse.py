"""Tests for parse_judge_output()."""

import harness


def test_parse_valid() -> None:
    assert harness.parse_judge_output('{"score": 4, "reason": "close"}') == (4, "close")


def test_parse_with_code_fences() -> None:
    text = '```json\n{"score": 5, "reason": "great"}\n```'
    assert harness.parse_judge_output(text) == (5, "great")


def test_parse_with_surrounding_prose() -> None:
    text = 'Sure! Here is the grade: {"score": 2, "reason": "wrong value"} thanks'
    assert harness.parse_judge_output(text) == (2, "wrong value")


def test_parse_invalid_json() -> None:
    assert harness.parse_judge_output("{score: 4}") is None


def test_parse_no_json_object() -> None:
    assert harness.parse_judge_output("I give it a 4 out of 5.") is None


def test_parse_out_of_range_high() -> None:
    assert harness.parse_judge_output('{"score": 6, "reason": "x"}') is None


def test_parse_out_of_range_low() -> None:
    assert harness.parse_judge_output('{"score": 0, "reason": "x"}') is None


def test_parse_non_integer_score() -> None:
    assert harness.parse_judge_output('{"score": "4", "reason": "x"}') is None
    assert harness.parse_judge_output('{"score": true, "reason": "x"}') is None


def test_parse_missing_reason() -> None:
    assert harness.parse_judge_output('{"score": 4}') is None


def test_parse_non_dict_json() -> None:
    assert harness.parse_judge_output('[{"score": 4, "reason": "x"}]') is None