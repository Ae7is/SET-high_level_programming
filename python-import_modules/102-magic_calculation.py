#!/usr/bin/python3
"""Do a magic calculation."""


def magic_calculation(a, b):
    """Perform the calculation shown by the bytecode."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
