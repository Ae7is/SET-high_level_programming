#!/usr/bin/python3
"""Module that defines the function read_file."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout.

    Args:
        filename (str): the path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
