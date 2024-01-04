#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """A rectangle object."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width: width of the rectangle
            height" height of the rectangle
        Raises:
            TypeError: width and height must be integers
            ValueError: width and height must be greater than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves width.

        Returns: width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Retrieves height.

        Returns: height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the value of width.

        Args:
            value: value to set the width
        Raises:
            TypeError: value must be an integer
            ValueError: valule must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value of height.

        Args:
            value: value to set the width
        Raises:
            TypeError: value must be an integer
            ValueError: value must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """calculates the area of the rectangle.

        Returns: the area of the rectangle
        """
        return ((self.__width) * (self.__height))

    def perimeter(self):
        """Calculates the perimeter of the rectangel.

        Returns: the perimeter of the rectangle
        """
        return ((self.__width * 2) + (self.__height * 2))
