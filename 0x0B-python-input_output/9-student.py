#!/usr/bin/python3
"""Student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance with first_name, last_nameage"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
