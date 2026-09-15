#!/usr/bin/python3
"""Module that replaces an element in a copy of a list, C-array style."""


def new_in_list(my_list, idx, element):
    """Return a copy of my_list with the element at idx replaced.

    Args:
        my_list: the original list
        idx: the index of the element to replace (non-negative)
        element: the new value to place at idx

    Returns:
        A new list with the element replaced, or an unmodified
        copy of my_list if idx is negative or out of range.
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
