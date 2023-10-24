#!/usr/bin/python3
# 4-square.py by Ismael
"""A module for Square definition."""


class Square:
    """A square class that reperesents the shape."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: size of the current square
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
        """Retrieve size.

        Returns: size of the current square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter method.

        Args:
            value: value to set size
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of the square.

        Returns: area of the square
        """
        return self.__size ** 2
