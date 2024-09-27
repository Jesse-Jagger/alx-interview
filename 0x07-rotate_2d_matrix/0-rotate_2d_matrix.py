#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """rotates two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for l in range(int(n / 2)):
        y = (n - l - 1)
        for j in range(l, y):
            x = (n - 1 - j)
            # current number
            tmp = matrix[l][j]
            # change top for left
            matrix[l][j] = matrix[x][l]
            # change left for bottom
            matrix[x][l] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = tmp
