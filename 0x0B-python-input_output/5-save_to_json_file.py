#!/usr/bin/python3
"""Module with a function to save an object to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file.

    Args:
        my_obj (object): The Python object to be saved.
        filename (str): The name of the JSON file.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
