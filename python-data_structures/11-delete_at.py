#!/usr/bin/python3
"""Module that deletes an item at a specific index in a list."""


def delete_at(my_list=[], idx=0):
    """Delete the item at idx from my_list, in place.

    Args:
        my_list: the list to modify
        idx: the index of the item to delete (non-negative)

    Returns:
        The list, with the item at idx removed if idx was valid,
        unchanged otherwise.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
