#!/usr/bin/python3
"""Module that defines the function write_file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, replacing any old content.

    Args:
        filename (str): the path of the file to write.
        text (str): the text to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
