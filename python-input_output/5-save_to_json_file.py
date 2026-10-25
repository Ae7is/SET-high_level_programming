#!/usr/bin/python3
"""Module that defines the function save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using its JSON representation.

    Args:
        my_obj: the object to serialize.
        filename (str): the path of the file to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
