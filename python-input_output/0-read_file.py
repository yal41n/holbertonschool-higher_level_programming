#!/usr/bin/python3
"""
Module that provides a function for reading and printing a text file.

This module contains the read_file function, which reads a UTF-8 text file
and prints its contents to standard output exactly as stored.
"""


def read_file(filename=""):
    """
    Read a text file (UTF-8) and print its content to stdout.

    Args:
        filename (str): The path to the text file to read.

    The function uses the with statement and does not handle exceptions
    related to file permissions or missing files, as per project requirements.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
