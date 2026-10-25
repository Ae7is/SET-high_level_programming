#!/usr/bin/python3
"""Module that defines the function lookup."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.
    """
    return dir(obj)
