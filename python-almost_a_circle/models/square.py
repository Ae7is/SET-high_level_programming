#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the square size."""
        self.width = value
        self.height = value
