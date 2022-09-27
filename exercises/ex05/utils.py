"""Continuing to build list utility functions."""
__author__ = "730477270"


from multiprocessing.dummy import Pool


def only_evens(xs: list[int]) -> list[int]:
    """Returns all even integers of a list in a new list."""
    even_numbers: list[int] = []
    for item in xs:
        if item % 2 == 0:
            even_numbers.append(item)
    return even_numbers

def concat(a: list[int], b: list[int]) -> list[int]:
    """Returns a new list containing the elements of first list followed by second list."""
    combined_list: list[int] = []
    for item in a:
        combined_list.append(item)
    for item in b:
        combined_list.append(item)
    return combined_list

def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns a list which is a subset of a given list, between the specified start index and the end index -1."""
    sublist: list[int] = []
    i: int = start
    g: int = end - 1
    if g > len(xs):
        g = len(xs)
    if i < 0:
        i = 0
    if len(xs) == 0 or i > len(xs) or g <= 0:
        return []
    while i < len(xs) and i <= g:
        sublist.append(xs[i])
        i += 1
    return sublist

