#!/usr/bin/python3
"""
Module that provides a function for saving Python objects to a JSON file.

This module contains the save_to_json_file function, which serializes a
Python object to JSON and writes it to a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
