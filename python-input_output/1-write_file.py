#!/usr/bin/python3
"""
Module that provides a function for writing text to a file.

This module contains the write_file function, which writes a UTF-8
string to a file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of
    characters written.

    Args:
        filename (str): The file to write to.
        text (str): The string to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
