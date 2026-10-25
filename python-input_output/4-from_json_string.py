#!/usr/bin/python3
"""Module that defines the function from_json_string."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): the JSON string.
    """
    return json.loads(my_str)
