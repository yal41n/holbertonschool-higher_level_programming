#!/usr/bin/python3
"""
4-inherits_from.py: Defines a function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    This function returns True if:
    1. The type of obj is a subclass of a_class.
    2. The type of obj is not the same as a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check inheritance against.

    Returns:
        bool: True if the object's class is a subclass of a_class,
              but not a_class itself; False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
