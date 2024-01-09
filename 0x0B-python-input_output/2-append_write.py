#!/usr/bin/python3
"""Module with a function to append a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append the given string to the specified text file (UTF8).

    If the file doesn’t exist, it will be created.

    Args:
        filename (str): The name of the text file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
