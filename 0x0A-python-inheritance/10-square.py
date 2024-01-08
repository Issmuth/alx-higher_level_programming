#!/usr/bin/python3
"""Module for square definition."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines an equilateral rectangle :)."""

    def __init__(self, size):
        """Instantiates a square object.

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
