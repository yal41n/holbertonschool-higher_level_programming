#!/usr/bin/python3
"""Function that prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            print(" ".join("{:d}".format(i) for i in row))
        else:
            print()
