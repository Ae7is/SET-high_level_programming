#!/usr/bin/python3
"""Module that adds two integers.

This module defines the function add_integer, which adds two numbers
after checking that both of them are integers or floats. Floats are
cast to integers before the addition is done.
"""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Args:
        a (int or float): the first number.
        b (int or float): the second number, 98 by default.

    Returns:
        The addition of a and b, as an integer.

    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
