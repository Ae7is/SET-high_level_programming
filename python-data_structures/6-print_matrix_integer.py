#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line.

    Args:
        matrix: a list of lists of integers
    """
    for row in matrix:
        print(" ".join("{}".format(num) for num in row))
