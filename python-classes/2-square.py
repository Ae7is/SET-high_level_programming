#!/usr/bin/python3
"""Module that defines a Square class with a validated size."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): the size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
