#!/usr/bin/python3
"""Module that multiplies two matrices with NumPy.

This module defines the function lazy_matrix_mul, which lets the NumPy
library do the work of multiplying two matrices instead of checking and
looping in plain Python.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (list): the first matrix.
        m_b (list): the second matrix.

    Returns:
        The matrix product of m_a and m_b, as a NumPy array.
    """
    return numpy.matmul(m_a, m_b)
