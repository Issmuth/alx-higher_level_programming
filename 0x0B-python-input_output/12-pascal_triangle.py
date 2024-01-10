#!/usr/bin/python3
"""Module for a function that creates
a list of lists of the pascal trangle rows."""


def pascal_triangle(n):
    """Returns a list of list(integers) representation
    of pascals triangle.

    Args:
        n: number of rows to return
    Returns:
        list of rows of the pascal triangle
    """
    if n == 0:
        return []

    init_row = [1]
    rows = []
    triangle = [init_row]

    if n == 1:
        return init_row

    for i in range(1, (n + 1)):
        for j in range(i):
            if j == 0:
                rows.append(1)
            else:
                rows.append(rows[j] + rows[j - 1])
            if  j == (n - 2):
                rows.app`end(1)
                break

        triangle.append(rows)
        rows = [1]

    return triangle
