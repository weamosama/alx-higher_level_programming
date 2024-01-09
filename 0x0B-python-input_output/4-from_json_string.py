#!/usr/bin/python3
"""Module with a function to return an object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Return the Python object represented by the given JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
