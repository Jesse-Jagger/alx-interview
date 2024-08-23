#!/usr/bin/python3
"""
This Calculates the fewest number of  operations needed in a CopyAll and Paste task
"""


def minOperations(n):
    """
    Calculates the minimum number of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    j = 1
    while n != 1:
        j += 1
        if n % j == 0:
            while n % j == 0:
                n /= j
                factor_list.append(j)
    return sum(factor_list)
