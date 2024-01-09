#!/usr/bin/python3
"""Student module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attributes to retrieve.

        Returns:
            dict: A dictionary representation of a Student instance.
        """
        # Check if attrs is a list
        if attrs is not None and not isinstance(attrs, list):
            raise TypeError("attrs must be a list or None")

        # If attrs is None, return the entire dictionary representation
        if attrs is None:
            return self.__dict__

        # Retrieve only the specified attributes
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
