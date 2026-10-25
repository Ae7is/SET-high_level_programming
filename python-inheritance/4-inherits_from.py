#!/usr/bin/python3
"""Module that defines the function inherits_from."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    An object that is exactly an instance of a_class does not count.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
