#!/usr/bin/python3
"""Module that prints integers of a list in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print each integer in my_list in reverse order, one per line.

    Args:
        my_list: a list of integers
    """
    for number in my_list[::-1]:
        print("{}".format(number))
