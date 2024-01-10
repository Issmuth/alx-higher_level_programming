#!/usr/bin/python3
"""Module for Student class definition."""


class Student:
    """Defines a student object."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object.

        Args:
            first_name: ...
            last_name: ...
            age: ...
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation
        a student instance.
        """
        return self.__dict__
