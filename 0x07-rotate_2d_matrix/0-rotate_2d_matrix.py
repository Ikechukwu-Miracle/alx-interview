#!/usr/bin/python3
"""In-Place rotation of NxN matirx"""


def rotate_2d_matrix(matrix):
    """Rotates n x n 2D matrix 90 degrees clockwise."""
    matrix.reverse()
    for x in range(len(matrix)):
        for y in range(x):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
