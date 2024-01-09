#!/usr/bin/python3
"""Student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance with first_name, last_name,age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance with optional filtering"""
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        else:
            return {attr: getattr(self, attr, None) for attr in attrs}
