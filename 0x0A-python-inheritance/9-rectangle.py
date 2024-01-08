#!/usr/bin/python3
"""Module for rectangle defintion"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle object"""

    def __init__(self, width, height):
        """Initializes a rectangle object.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates are of a rectangle.

        Returns: area of the rectangle
        """
        return ((self.__width) * (self.__height))

    def __str__(self):
         """Returns rectangle description."""	
         rep = "[" + str(self.__class__.__name__) + "] " 
         rep += str(self.__width) + "/" + str(self.__height)
         return rep
         
