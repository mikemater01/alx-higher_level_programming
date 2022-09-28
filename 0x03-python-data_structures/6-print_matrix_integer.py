#!/usr/bin/python3
# A function that prints a matrix of integers #

def print_matrix_integer(matrix=[[]]):
     if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
        return
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end="")
            if num == row[-1]:
                print()
            else:
                print(" ", end="")
