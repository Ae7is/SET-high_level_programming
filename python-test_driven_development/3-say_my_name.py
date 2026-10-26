#!/usr/bin/python3
"""Module that prints a name.

This module defines the function say_my_name, which prints the sentence
"My name is <first name> <last name>" after checking that both names
are strings.
"""


def say_my_name(first_name, last_name=""):
    """Print the sentence My name is <first name> <last name>.

    Args:
        first_name (str): the first name.
        last_name (str): the last name, empty by default.

    Raises:
        TypeError: if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
