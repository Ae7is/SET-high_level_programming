#!/usr/bin/python3
"""Module that defines the function append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a given string.

    Args:
        filename (str): the path of the file to change.
        search_string (str): the text to look for in each line.
        new_string (str): the text to insert after a matching line.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
