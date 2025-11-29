#!/usr/bin/python3
"""
Module that provides a function for appending text to a file.

This module contains the append_write function, which appends a UTF-8
string to a file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8) and return the
    number of characters added.

    If the file does not exist, it will be created.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
