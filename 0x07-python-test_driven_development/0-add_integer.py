#!/usr/bin/python3
"""A module that adds two integers"""


def add_integer(a, b=98):
    """A function that adds two integers
    Args:
        a: first integer
        b: second integer
    Returns:
        addition of two integers
    """
    if type(a) is not int or type(b) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
