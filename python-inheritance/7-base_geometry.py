#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an integer validator."""


class BaseGeometry:
    """A class that represents a geometry."""

    def area(self):
        """Raise an exception, because the area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Args:
            name (str): the name of the value, used in error messages.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
