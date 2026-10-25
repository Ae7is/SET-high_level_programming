#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """A class that represents a geometry."""

    def area(self):
        """Raise an exception, because the area is not implemented here."""
        raise Exception("area() is not implemented")
