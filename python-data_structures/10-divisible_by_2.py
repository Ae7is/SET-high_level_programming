#!/usr/bin/python3
"""Module that checks divisibility by 2 for each element in a list."""


def divisible_by_2(my_list=[]):
    """Check which elements of my_list are divisible by 2.

    Args:
        my_list: a list of integers

    Returns:
        A new list of the same size, with True where the
        corresponding element is divisible by 2, False otherwise.
    """
    return [number % 2 == 0 for number in my_list]
