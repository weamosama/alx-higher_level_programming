#!/usr/bin/python3
"""
===========================
Module with class BaseGeometry
===========================
"""


class BaseGeometry:
    """Base class for representing geometric shapes."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer: raise a TypeError exceptio.
        - If value is less or equal to 0: raise a ValueError.

        :param name: The name of the value.
        :param value: The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
