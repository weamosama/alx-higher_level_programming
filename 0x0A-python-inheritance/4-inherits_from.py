#!/usr/bin/python3
"""
==============================
Module with method inherits_from
==============================
"""


def inherits_from(obj, a_class):
    """
    Method that returns True if an object is an instance of a class
    from the specified class; otherwise, False.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a class that inherited
    """
    return issubclass(type(obj), a_class)
