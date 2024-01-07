#!/usr/bin/python3
"""
Prints My name is <first name> <last name>.

Args:
    first_name (str): First name.
    last_name (str, optional): Last name. Defaults to an empty string.

Raises:
    TypeError: If first_name or last_name is not a string.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Validate input types
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print("My name is {} {}".format(first_name, last_name))
