#!/usr/bin/python3
# 6-square.py by Ismael
"""Square definition module."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size: size of the square
            position: position based on the square
        Raises:
            TypeError: size must be an integer &
            position must be a tuple of 2 integers
            ValueError: size must be >= 0
        """
#        if not isinstance(size, int):
#           raise TypeError("size must be an integer")
#        if size < 0:
#            raise ValueError("size must be >= 0")
#        if len(position) != 2:
#            raise TypeError("position must be a tuple of 2 positive integers")
#        for i in position:
#            if not isinstance(i, int) or i < 0:
#                raise TypeError("position must be a tuple " +
#                               "of 2 positive integers")
#            break

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve size.

        Returns: size
        """
        return self.__size

    @property
    def position(self):
        """Retrieve position.

        Returns: position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """Set the value of size.

        Args:
            value: value to set
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the value of position.

        Args:
            value: value to set
        Raises:
            TypeError: position must be a tuple of 2
            positive integers
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple " +
                                "of 2 positive integers")
            break

        self.__position = position

    def area(self):
        """Calculate the area of the current square.

        Returns: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'."""
        pos = ""
        size = self.__size

        if size == 0:
            return "\n"
        for i in range(self.position[1]):
            print("\n", end="")
        for i in range(size):
            for j in range(self.position[0]):
                print(" ", end="")
            for k in range(size):
                print("#", end="")
            print("\n", end="")
