#!/usr/bin/python3
"""Module that removes all 'c' and 'C' characters from a string."""


def no_c(my_string):
    """Return a copy of my_string with all 'c' and 'C' removed.

    Args:
        my_string: the original string

    Returns:
        A new string with every 'c' and 'C' character removed.
    """
    return "".join(char for char in my_string if char not in "cC")
