#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple dat.
    """

    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return obj
