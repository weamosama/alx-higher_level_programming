#!/usr/bin/python3
"""Module with a function to return the JSON representation of an object."""

import json

def to_json_string(my_obj):
    """Return the JSON representation of the given object.

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
