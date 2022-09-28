#!/usr/bin/python3
''' A function that returns a set of all elements present in only one set '''

def only_diff_elements(set_1: set, set_2: set):
    return set_1.union(set_2) - set_1.intersection(set_2)
