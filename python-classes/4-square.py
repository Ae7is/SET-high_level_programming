#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
