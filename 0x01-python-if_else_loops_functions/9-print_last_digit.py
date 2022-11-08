#!/usr/bin/python3
"""Print the last digit of a number."""


def print_last_digit(number):
    if not type(number) is int:
        raise TypeError("Only integers are allowed")
    digit = str(number)[-1]
    print(digit, end="")
    return digit
