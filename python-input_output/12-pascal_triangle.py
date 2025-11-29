#!/usr/bin/python3
"""
Module that provides a function for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle
    of n.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
