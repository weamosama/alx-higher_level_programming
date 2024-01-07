#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ., ? and :

Args:
    text (str): The input text.

Raises:
    TypeError: If text is not a string.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Validate input type
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    current_line = ""

    # Iterate through each character in the text
    for char in text:
        # Add the character to the current line
        current_line += char

        # Check for specific characters
        if char in ['.', '?', ':']:
            # Print the current line without leading or trailing spaces
            print(current_line.strip())
            # Print an empty line
            print()
            # Reset the current line
            current_line = ""

    # Print any remaining content in the current line
    if current_line:
        print(current_line.strip())
