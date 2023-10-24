#!/bin/usr/python3
# 4-square.py by Ismael
""" Square definition"""


class Square:
    """ A square object"""
    def size __init__(self, size=0):
        """ initializes a square
        Args:
            size: size of the square
        Raises:
            TypeError: size must be integer
            ValueError: size must be >=0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")

        self.__size = size

    @property
    def size(self):
        """ retrieve size
        Returns: size of the current square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ size setter method
        Args:
            value: value to set size
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ calculates area of the square
        Returns: area of the square
        """

        return self.__size ** 2
