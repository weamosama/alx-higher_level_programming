#!/usr/bin/python3
"""
Divides all elements of a matrix.

Args:
    matrix (list of lists): Matrix of integers or floats.
    div (int or float): Number to divide each element of the matrix.

Returns:
    list of lists: New matrix with elements divided by div.

Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
    TypeError: If each row of the matrix does not have the same size.
    TypeError: If div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
"""


def matrix_divided(matrix, div):

    # Validate input types
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError
        ("matrix must be a list of lists of integers or floats")
    # Validate each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    result = [[round(element / div, 2) for element in row] for row in matrix]

    return result
