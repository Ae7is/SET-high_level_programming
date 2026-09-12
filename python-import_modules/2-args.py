#!/usr/bin/python3
"""Print the number and list of arguments."""

import sys


if __name__ == "__main__":
    count = len(sys.argv) - 1

    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
