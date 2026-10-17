#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): size of the square.
            x (int): horizontal offset.
            y (int): vertical offset.
            id (int): id of the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set width then height with the same validated value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes.

        Args:
            *args: id, size, x, y in this order.
            **kwargs: attribute names with their values. Ignored when
                args is not empty.
        """
        names = ["id", "size", "x", "y"]
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if key in names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "x": self.x, "size": self.size,
                "y": self.y}
