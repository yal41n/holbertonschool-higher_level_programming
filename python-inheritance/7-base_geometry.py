#!/usr/bin/python3
"""Defines a BaseGeometry class with area and integer validator methods."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:  # <-- fixes bool issue
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
