#!/usr/bin/python3
"""
Module that defines a class MyList which inherits from list.
"""


class MyList(list):
    """
    Represents a list with an additional method to print a sorted version.
    """

    def print_sorted(self):
        """
        Print the list in ascending order without modifying the original list.
        """
        print(sorted(self))
