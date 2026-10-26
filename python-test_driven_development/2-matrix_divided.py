#!/usr/bin/python3
"""Module that divides all the elements of a matrix.

This module defines the function matrix_divided. It checks that the
matrix is a list of lists of integers or floats, that every row has the
same size and that the divisor is a number that is not zero.
"""


def matrix_divided(matrix, div):
    """Divide all the elements of a matrix by a number.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int or float): the number to divide by.

    Returns:
        A new matrix with each element divided by div and rounded to
        2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of numbers, if the
            rows do not have the same size, or if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
