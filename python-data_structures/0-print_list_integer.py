#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line."""
    for number in my_list:
        print("{:d}".format(number))
