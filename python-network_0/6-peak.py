#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Return a peak of the list, or None if the list is empty.

    A peak is an element that is not smaller than its neighbors.
    The search halves the range each step, so the complexity is O(log(n)).
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
