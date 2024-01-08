#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: List of attribute names.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
