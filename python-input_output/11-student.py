#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


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

    def to_json(self, attrs=None):
        """Return the dictionary description of the student.

        Args:
            attrs (list): names of the attributes to keep. When it is not
                a list of strings, every attribute is returned.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {a: self.__dict__[a] for a in attrs if a in self.__dict__}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace the attributes of the student with those of a dictionary.

        Args:
            json (dict): attribute names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
