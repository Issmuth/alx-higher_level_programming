#!/usr/bin/python3
"""Rectangle class definition module."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class defintion."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor.

        Args:
            width: width of rectangle
            height: height of rectangle
            x: ...
            y: ...
            id: id of the rectangle object
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Retrieve width of current instance.

        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width.

        Args:
            value: value of width to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height of current instance.

        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height.

        Args:
            value: value of height to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve x of current instance.

        Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x.

        Args:
            value: value of x to set
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y of current instance.

        Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of y.

        Args:
            value: value of y to set
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle instance.

        Returns: Area of the rectangle.
        """
        return ((self.__height) * (self.__width))

    def display(self):
        """Prints the rectangle using '#'."""
        for k in range(self.__y):
            print()

        indent = ""
        for h in range(self.__x):
            indent += " "

        for i in range(self.__height):
            print("{}".format(indent), end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the string representation of a rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updates the attributes of a rectangle instance.

        Args:
            args: tuple of arguments to update
                1st argument: id attribute
                2nd argument: width attribute
                3rd argument: height attribute
                4th argument: x attribute
                5th argument: y attribute
        """
        size = len(args)
        if size != 0:
            for i in range(size):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                else:
                    pass

    def to_dictionary(self):
        """Returns the dictionary representation a rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
