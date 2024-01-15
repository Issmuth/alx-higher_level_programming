#!/usr/bin/python3
"""Square definition module."""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square instance.

        Args:
            size: dimension of the square
            x: ...
            y: ...
            id: id of the square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation fo the square."""

        return ("[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value: value of size to set.
        """
        self.width = value

    def update(self, *args, **kwargs):
        """Updates the content of a square instance.

        Args:
            args: tuple set of arguments
                1st argument: id
                2nd argument: size
                3rd argument: x
                4th argument: y
            kwargs: dictionary set of arguments
        """
        size = len(args)
        if size != 0:
            if size == 1:
                super().update(args[0])
            elif size == 2:
                super().update(args[0], args[1], args[1])
            elif size == 3:
                super().update(args[0], args[1], args[1], args[2])
            elif size == 4:
                super().update(args[0], args[1], args[1], args[2], args[3])
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.x
        }
