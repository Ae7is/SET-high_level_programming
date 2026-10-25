#!/usr/bin/python3
"""Module that defines the function to_json_string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: the object to serialize.
    """
    return json.dumps(my_obj)
