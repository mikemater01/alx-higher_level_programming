#!/usr/bin/python3
"""More Returns."""


def multiple_returns(sentence):
    if len(sentence) == 0:
        return (len(sentence), None)
    return (len(sentence), sentence[0])
