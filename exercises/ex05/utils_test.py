"""Unit tests for utils functions."""
__author__ = "730477270"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub

def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]

def test_only_evens_more_items() -> None:
    xs: list[int] = [-4, 0, 31, 46, 99, 122]
    assert only_evens(xs) == [-4, 0, 46, 122]

def test_concat_single_item() -> None:
    a: list[int] = [4]
    b: list[int] = [9]
    assert concat(a, b) == [4, 9]

def test_concat_multiple_items() -> None:
    a: list[int] = [456, 248, 32229]
    b: list[int] = [9, 56, 12003, 573, 82]
    assert concat(a, b) == [456, 248, 32229, 9, 56, 12003, 573, 82]

def test_concat_more_items() -> None:
    a: list[int] = [-6, -100, 5, 9, 234]
    b: list[int] = [956, -1, 17]
    assert concat(a, b) == [-6, -100, 5, 9, 234, 956, -1, 17]

def test_sub_empty_list() -> None:
    xs: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == []

def test_sub_negative_start() -> None:
    xs: list[int] = [45, 6, 395, -8, 10]
    start: int = -7
    end: int = 4
    assert sub(xs, start, end) == [45, 6, 395, -8]

def test_sub_end_greater_than_length() -> None:
    xs: list[int] = [67, 4, 1, 98, -5, 693]
    start: int = 0
    end: int = 45
    assert sub(xs, start, end) == [67, 4, 1, 98, -5, 693]
