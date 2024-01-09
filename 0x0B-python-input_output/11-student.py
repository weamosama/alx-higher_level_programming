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
            attrs (list): A list of attributes to retrieve

        Returns:
            dict: A dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

