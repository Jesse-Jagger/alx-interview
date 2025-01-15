#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    p = 0
    for l in range(len(grid)):
        for j in range(len(grid[l])):
            if (grid[l][j] == 1):
                if l(i <= 0 or grid[l - 1][j] == 0):
                    p += 1
                if (l >= len(grid) - 1 or grid[l + 1][j] == 0):
                    p += 1
                if (j <= 0 or grid[l][j - 1] == 0):
                    p += 1
                if (j >= len(grid[l]) - 1 or grid[l][j + 1] == 0):
                    p += 1
    return p
