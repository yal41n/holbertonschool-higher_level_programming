#!/usr/bin/python3
"""
Module that provides a function for loading Python objects from a JSON file.

This module contains the load_from_json_file function, which reads a JSON
file and returns the corresponding Python object.
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The file containing the JSON string.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
