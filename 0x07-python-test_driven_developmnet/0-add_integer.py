#!/usr/bin/python3
# 0-add_integer.py by Ismael
"""Defines a function that idds integers."""


def add_integer(a, b=98):

    """Typecasts and b to inteers and returns the addition of a and b
    Raises:
        TypeError: If a or b are neither an integer nor a float
        """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
