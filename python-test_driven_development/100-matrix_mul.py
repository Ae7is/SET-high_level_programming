#!/usr/bin/python3
"""Module that multiplies two matrices.

This module defines the function matrix_mul, which checks that both
matrices are valid lists of lists of integers or floats and then
returns their matrix product.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list): the first matrix, a list of lists of numbers.
        m_b (list): the second matrix, a list of lists of numbers.

    Returns:
        The matrix product of m_a and m_b, as a list of lists.

    Raises:
        TypeError: if a matrix is not a list, not a list of lists, has
            elements that are not numbers or has rows of different sizes.
        ValueError: if a matrix is empty or if the matrices cannot be
            multiplied.
    """
    matrices = (("m_a", m_a), ("m_b", m_b))

    for name, matrix in matrices:
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))

    for name, matrix in matrices:
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("{} must be a list of lists".format(name))

    for name, matrix in matrices:
        if matrix == [] or matrix == [[]]:
            raise ValueError("{} can't be empty".format(name))

    for name, matrix in matrices:
        for row in matrix:
            for item in row:
                if not isinstance(item, (int, float)):
                    msg = "{} should contain only integers or floats"
                    raise TypeError(msg.format(name))

    for name, matrix in matrices:
        for row in matrix:
            if len(row) != len(matrix[0]):
                msg = "each row of {} must be of the same size"
                raise TypeError(msg.format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row in m_a:
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += row[k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result
