#!/usr/bin/python3
"""Module that defines the function append_write."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file.

    The file is created if it does not exist.

    Args:
        filename (str): the path of the file.
        text (str): the text to add.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
