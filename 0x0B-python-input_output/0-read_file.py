#!/usr/bin/python3
"""Module with a function to read and print the contents of a text file."""

def read_file(filename=""):
    """Read the content of the given text file and print it to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
