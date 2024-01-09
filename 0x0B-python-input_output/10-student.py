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
    """
    Retrieves a dictionary representation of a Student instance.

    Args:
        attrs (list): A list of attributes to include in the dictionary.

    Returns:
        dict: A dictionary representation of the Student instance.
    """
    if attrs is not None and not isinstance(attrs, list):
        raise TypeError("attrs must be a list or None")

    if attrs is None:
        return self.__dict__
    
    return {key: getattr(self, key, None) for key in attrs if hasattr(self, key)}
