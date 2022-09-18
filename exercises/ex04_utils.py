"""Implementing algorithms and practicing lists."""

__author__ = "730477270"


def all(a: list[int], b: int) -> bool:
    """Given a list of ints and an int, returns whether or not all ints in list are equal to given int."""
    i: int = 0
    length: int = len(a)
    indicator: bool = True
    while i < length:
        if b != a[i] or length == 0:
            indicator = False
        i = i + 1
    return indicator


def max(input: list[int]) -> int:
    """Given a list of ints, returns the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest_number: int = input[0]
    i: int = 0
    while i < len(input):
        if input[i] > largest_number:
           largest_number = input[i]
        i = i + 1
    return largest_number
        

def is_equal(a: list[int], b: list[int]) -> bool:
    """Given two lists of int values, returns whether or not lists are identical."""
    i: int = 0
    indicator = False
    if len(a) != len(b):
        return indicator
    while i < len(a) and len(b):
        if a[i] != b[i]:
            indicator = False
        i += 1
    if a == b:
        indicator = True
    return indicator