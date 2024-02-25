#!/usr/bin/python3
"""0-rotate_2d_matrix.py module"""


def rotate_2d_matrix(matrix):
    """Function to rotate a 2d matrix in-place"""

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
