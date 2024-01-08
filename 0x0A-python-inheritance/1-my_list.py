#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""

class MyList(list):
    """Class with method print_sorted"""

    def print_sorted(self):
        """Method that prints the list sorted in ascending order"""
        print(sorted(self))
