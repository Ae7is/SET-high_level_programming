#!/usr/bin/python3
"""Module that defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list that can print itself in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order.

        The list itself is not changed.
        """
        print(sorted(self))
