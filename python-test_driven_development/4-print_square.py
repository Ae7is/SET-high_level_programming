#!/usr/bin/python3
"""Module that prints a square.

This module defines the function print_square, which prints a square
made of the character # after checking that its size is an integer
that is not negative.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): the length of each side of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
