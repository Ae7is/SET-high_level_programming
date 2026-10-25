#!/usr/bin/python3
"""Module that defines the function load_from_json_file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): the path of the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
