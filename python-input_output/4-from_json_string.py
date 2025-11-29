#!/usr/bin/python3
"""
Module that provides a function for converting JSON strings to objects.

This module contains the from_json_string function, which returns the
corresponding Python data structure represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to decode.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
