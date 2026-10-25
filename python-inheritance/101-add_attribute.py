#!/usr/bin/python3
"""Module that defines the function add_attribute."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it is possible.

    Args:
        obj: the object to change.
        name (str): the name of the new attribute.
        value: the value of the new attribute.

    Raises:
        TypeError: if the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
