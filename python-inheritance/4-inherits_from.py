#!/usr/bin/python3
"""Module defining a function to check if an object is a subclass instance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
