#!/usr/bin/python3
"""
1-rectangle.py: Defines a class Rectangle with private width and height attributes,
validated by property getters and setters.
"""


class Rectangle:
    """
    Defines a rectangle with optional width and height, ensuring they are
    non-negative integers.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the private instance attribute __width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the private instance attribute __width, performing validation.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the private instance attribute __height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the private instance attribute __height, performing validation.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
