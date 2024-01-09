#!/usr/bin/python3
"""Module with a function to load an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
