#!/usr/bin/python3
"""Module with a function to save an object to a text file using JSOn"""

import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of the given object to a text file.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the text file to write.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
