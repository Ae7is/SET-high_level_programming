#!/usr/bin/python3
"""Module that defines a class that limits its instance attributes."""


class LockedClass:
    """Allows only the instance attribute first_name."""

    __slots__ = ["first_name"]
