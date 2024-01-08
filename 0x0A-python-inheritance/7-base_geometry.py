#!/usr/bin/python3
"""Module that defines BaseGeometry class."""


class BaseGeometry:
    """Defines a base geometry class."""

    def area(self):
        """raises an exception with implementation error message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value.

        Args:
            name: string
            value: integer greater than zero
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must an integer".format(name))

        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
