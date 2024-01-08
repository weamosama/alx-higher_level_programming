#!/usr/bin/python3
"""
========================
Module with class MyInt
========================
"""


class MyInt(int):
    """Class representing a rebellious integer."""

    def __eq__(self, other):
        """Override the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        return super().__eq__(other)
