#!/usr/bin/python3
"""Script to load, add, and save items to a Python list."""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    # Load existing data from the file
    my_list = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    # If the file doesn't exist or is not a valid JSON, start with an empty list
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
