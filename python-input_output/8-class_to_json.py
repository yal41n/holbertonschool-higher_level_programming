#!/usr/bin/python3
"""
Module that provides a function for converting a class instance to a
dictionary suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object's attributes.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all attributes of obj.
    """
    return obj.__dict__.copy()
