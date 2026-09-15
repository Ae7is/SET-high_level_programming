#!/usr/bin/python3
def element_at(my_list, idx):
    """Return the element at idx, or None if idx is invalid.

    Args:
        my_list: the list to search
        idx: the index of the element to retrieve (non-negative)

    Returns:
        The element at idx, or None if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
