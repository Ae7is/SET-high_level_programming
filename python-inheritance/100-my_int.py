#!/usr/bin/python3
"""Module that defines MyInt, an integer with inverted comparisons."""


class MyInt(int):
    """An integer that is a rebel: == and != are inverted."""

    def __eq__(self, other):
        """Return True when the values are different."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True when the values are equal."""
        return int.__eq__(self, other)
