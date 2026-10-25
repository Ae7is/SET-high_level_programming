#!/usr/bin/python3
"""Module that defines the function pascal_triangle."""


def pascal_triangle(n):
    """Return the Pascal's triangle of n as a list of lists of integers.

    Args:
        n (int): the number of rows. A value of 0 or less gives [].
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(n - 1):
        previous = triangle[-1]
        row = [1]
        for i in range(len(previous) - 1):
            row.append(previous[i] + previous[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
