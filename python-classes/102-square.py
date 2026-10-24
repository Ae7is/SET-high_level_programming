#!/usr/bin/python3
"""Module that defines a Square class that can be compared by area."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int or float): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validation."""
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the squares have different areas."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square has a smaller area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square has a smaller or equal area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square has a larger area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square has a larger or equal area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
