#!/usr/bin/python3
"""
======================================
Module with method is_kind_of_class
======================================
"""


def is_kind_of_class(obj, a_class):
    """
    Method that returns True if an object is an instance 
    inherited from, the specified class; otherwise, False.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a_class or its subclass False.
    """
    return isinstance(obj, a_class)
