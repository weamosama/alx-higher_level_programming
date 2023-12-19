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

    @property
    def size(self):
        """
        Getter method for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Method documentation goes here
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method documentation goes here
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
