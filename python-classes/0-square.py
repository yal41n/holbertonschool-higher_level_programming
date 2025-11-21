#!/usr/bin/python3
"""
This module defines a Square class that represents a geometric square.
The class currently stores only the size, which is kept private.
"""


class Square:
    """
    Represents a square.

    This class defines a square by storing its size as a private instance
    attribute. The value is not validated here because later tasks will add
    getter/setter logic and proper validation.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size: The size of the square. No type or value checking is done.
        """
        self.__size = size
