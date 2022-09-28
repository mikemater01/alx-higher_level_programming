#!/usr/bin/python3
# A function that retrives an element from a list like in C #

def element_at(my_list, idx):
    if idx < 0or idx >= len(my_list):
        return None
    return my_list[idx]
