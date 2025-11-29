#!/usr/bin/python3
"""
Pickling Custom Classes Module

Provides a CustomObject class that can be serialized and deserialized
using the pickle module. Handles errors for missing or corrupted files.
"""
import pickle


class CustomObject:
    """
    Custom object with name, age, and is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject instance.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The file to save the object to.

        Returns:
            None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject or None: The deserialized object or None on error.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (OSError, pickle.PickleError, EOFError):
            return None
