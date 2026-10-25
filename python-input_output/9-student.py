#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """A student with a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Create a student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description of the student."""
        return self.__dict__.copy()
