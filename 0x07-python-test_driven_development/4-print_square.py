#!/usr/bin/python3
"""
Prints a square with the character #.

Args:
    size (int): The size length of the square.

Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    TypeError: If size is a float and is less than 0.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.
    """
    # Validate input type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Validate input value
    if size < 0:
        raise ValueError("size must be >= 0")

    # Validate input value as an integer
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for i in range(size):
        print("#" * size)
