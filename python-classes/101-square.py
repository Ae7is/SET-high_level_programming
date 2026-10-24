#!/usr/bin/python3
"""Module that defines a Square class that prints like my_print."""


class Square:
    """Defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): the size of the square.
            position (tuple): the offset used when printing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validation."""
        msg = "position must be a tuple of 2 positive integer"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(msg)
        for item in value:
            if type(item) is not int or item < 0:
                raise TypeError(msg)
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, using the position."""
        print(str(self))

    def __str__(self):
        """Return the square drawn with #, using the position."""
        if self.__size == 0:
            return ""
        rows = [" " * self.__position[0] + "#" * self.__size
                for _ in range(self.__size)]
        return "\n" * self.__position[1] + "\n".join(rows)
