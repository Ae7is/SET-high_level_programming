#!/usr/bin/python3
"""Module that adds two tuples of integers."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise, treating missing values as 0.

    Args:
        tuple_a: first tuple of integers
        tuple_b: second tuple of integers

    Returns:
        A tuple with the sum of the first elements and the sum
        of the second elements of each input tuple.
    """
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
