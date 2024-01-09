#!/usr/bin/python3
"""Module with a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write the given string to the specified text file (UTF8).

    Args:
        filename (str): The name of the text file to write.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
