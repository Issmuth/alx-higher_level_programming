#!/usr/bin/python3
# 3-square.py by Ismael
"""Square Object Definition."""


class Square:
    """a square object."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: size of a square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less that zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate the current square area.

        Returns: area of the current square
        """
        return (self.__size ** 2)
