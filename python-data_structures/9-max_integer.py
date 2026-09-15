#!/usr/bin/python3
"""Module that finds the biggest integer in a list."""


def max_integer(my_list=[]):
    """Find and return the largest integer in my_list.

    Args:
        my_list: a list of integers

    Returns:
        The largest integer in my_list, or None if the list is empty.
    """
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for number in my_list:
        if number > biggest:
            biggest = number
    return biggest
