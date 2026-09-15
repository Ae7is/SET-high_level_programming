#!/usr/bin/python3
"""Module that returns a string's length and its first character."""


def multiple_returns(sentence):
    """Return the length of sentence and its first character.

    Args:
        sentence: the string to analyze

    Returns:
        A tuple (length, first_character). first_character is
        None if sentence is empty.
    """
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return len(sentence), first_char
