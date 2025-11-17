#!/usr/bin/python3
"""Function that removes all characters c and C from a string"""


def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
