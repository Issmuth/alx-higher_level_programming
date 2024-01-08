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

    def area(self):
        """calculates the area of a square."""
        return (self.__size ** 2)

    def __str__(self):
        """Returns the string representation of the square."""
        rep = "[" + str(self.__class__.__name__) + "] "
        rep += str(self.__size) + "/" + str(self.__size)
        return rep
