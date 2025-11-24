#!/usr/bin/python3
"""Defines a BaseGeometry class with area method."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")
