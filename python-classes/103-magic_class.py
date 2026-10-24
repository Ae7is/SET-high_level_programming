#!/usr/bin/python3
"""Module that defines a MagicClass that describes a circle."""
import math


class MagicClass:
    """Defines a circle by its radius."""

    def __init__(self, radius=0):
        """Initialize a new circle.

        Args:
            radius (int or float): the radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
