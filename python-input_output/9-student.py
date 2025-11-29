#!/usr/bin/python3
"""
Module that defines a Student class.
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

    def to_json(self):
        """
        Return the dictionary representation of the Student instance.

        Returns:
            dict: Dictionary containing all attributes of the student.
        """
        return self.__dict__.copy()
