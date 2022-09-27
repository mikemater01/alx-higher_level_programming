#!/usr/bin/python3
# A function that removes all characters c and C from a string #

def no_c(my_string):
    new_str = ""
    for character in my_string:
        if character not in ['c', 'C']:
            new_str += character
    return new_str
