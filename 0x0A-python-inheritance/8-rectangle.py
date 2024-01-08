#!/usr/bin/python3
"""
=======================
Module with class Rectangle
=======================
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""
    def __init__(self, width, height):
        """Initialize the Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
