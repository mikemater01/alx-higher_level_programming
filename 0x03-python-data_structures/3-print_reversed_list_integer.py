#!/usr/bin/python3
# A function that prints all integers of a list, in reverse order #

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for num in my_list[::-1]:
        print("{:d}".format(num))


if __name__== '__main__':
    print_reversed_list_integer()
