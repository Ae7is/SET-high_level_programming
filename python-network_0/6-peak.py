#!/usr/bin/python3
"""Algorithm to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers using binary search O(log(n))."""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        # If the element is smaller than the next one, the peak must be to the right
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        # Otherwise, the peak is the current element or to the left
        else:
            high = mid

    return list_of_integers[low]
