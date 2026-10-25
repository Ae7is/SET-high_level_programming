#!/usr/bin/python3
"""Module that defines a Square class with its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a private size."""

    def __init__(self, size):
        """Create a square after validating its size.

        Args:
            size (int): the size, a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the description [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
