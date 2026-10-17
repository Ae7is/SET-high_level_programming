#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): horizontal offset.
            y (int): vertical offset.
            id (int): id of the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x offset."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x offset after validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y offset."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y offset after validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #, using x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes.

        Args:
            *args: id, width, height, x, y in this order.
            **kwargs: attribute names with their values. Ignored when
                args is not empty.
        """
        names = ["id", "width", "height", "x", "y"]
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if key in names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
