#!/usr/bin/python3
"""Check if a character is lowercase."""


def islower(c):
    return (ord(c) >= ord('a') and ord(c) <= ord('z'))
