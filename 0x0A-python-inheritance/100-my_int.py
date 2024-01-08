#!/usr/bin/python3
"""Module that defines class MyInt"""


class MyInt(int):
    """Defines our rebel."""

    def __eq__(self, value):
        """Reverses the '==' operation."""
        return self.real != value

    def __neq__(self, value):
        """Reverses the '!=' operation."""
        return self.real == value
