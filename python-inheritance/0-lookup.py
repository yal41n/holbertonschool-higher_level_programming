#!/usr/bin/python3
"""
Module that defines a function to list attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: List of strings representing the object's attributes and methods.
    """
    return dir(obj)
