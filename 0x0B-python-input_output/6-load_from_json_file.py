#!/usr/bin/python3
"""Module with a function to create an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Create an object from the JSON representation in the specified file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(fiile)
