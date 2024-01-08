#!/usr/bin/python3
"""
=============================
Module with the class MyList
=============================
"""


class MyList(list):
    """A class that inherits from list and provides additional methods."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
