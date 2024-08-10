#!/usr/bin/python3
"""Pascal Triangle"""

def pascal_triangle(n):
    """prints a Triangle"""
    
    if n <= 0:
        return []
    triangle = [[1]]
    for row_number in range(1, n):
        row = [1]
        for k in range(1, row_number):
            element = triangle[row_number - 1][k - 1] + triangle[row_number - 1][k]
            row.append(element)
        row.append(1)
        triangle.append(row)

    return triangle
