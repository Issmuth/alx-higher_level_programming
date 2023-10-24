#!/usr/bin/python3
# 5-square.py by Ismael
"""Square definition module."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrive size of current square.

        Returns: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of a square.

        Args:
            value: value of size
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
        """Calculate area of current square.

        Returns: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'."""
        size = self.__size
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
        if size == 0:
            print()
