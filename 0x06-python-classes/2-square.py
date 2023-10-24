#!/usr/bin/python3
# 2-square.py by Ismael
""" Square defintion"""


class Square:
    """ A square object"""
    def __init__(self, size=0):
        """ initialize a Square object
        Args: size - size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
