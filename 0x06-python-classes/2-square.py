#!/usr/bin/python3
"""
Module documentation goes here
"""

class Square:
    """
    Class documentation goes here
    """
    def __init__(self, size=0):
        """
        Method documentation goes here
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
