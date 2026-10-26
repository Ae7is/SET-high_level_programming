#!/usr/bin/python3
"""Module that prints a text with indentation.

This module defines the function text_indentation, which prints a text
and adds two new lines after each of the characters ., ? and :
without leaving spaces at the start or at the end of the printed lines.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each of . ? and :

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(), end="\n\n")
            line = ""
    print(line.strip(), end="")
