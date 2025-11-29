#!/usr/bin/python3
"""
Module that defines a Student class with JSON serialization and
deserialization capabilities.
"""


class Student:
    """
    Class that defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in this list are
        included. Otherwise, all attributes are included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary of selected attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with those from
        a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
