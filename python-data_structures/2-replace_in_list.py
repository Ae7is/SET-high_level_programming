#!/usr/bin/python3
"""Module that replaces an element in a list, C-array style."""


def replace_in_list(my_list, idx, element):
    """Replace the element at idx with a new value.

    Args:
        my_list: the list to modify
        idx: the index of the element to replace (non-negative)
        element: the new value to place at idx

    Returns:
        The list, modified if idx was valid, unchanged otherwise.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
