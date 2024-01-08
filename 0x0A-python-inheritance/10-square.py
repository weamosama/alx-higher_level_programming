#!/usr/bin/python3
"""
===================
Module with class Square
===================
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initialize the Square instance with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
