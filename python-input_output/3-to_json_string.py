#!/usr/bin/python3
"""
Module that provides a function for converting Python objects to JSON.

This module contains the to_json_string function, which returns the
JSON representation of a Python object as a string.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
