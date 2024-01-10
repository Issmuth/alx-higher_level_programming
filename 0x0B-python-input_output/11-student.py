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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation
        a student instance.
        """
        data = self.__dict__
        if (attrs is None or type(attrs) != list or
                any(type(elements) != str for elements in attrs)):
            return data

        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        instance.

        Args:
            json: json is a dictionary that used to repalce
        """
        for key, value in json.items()
            setattr(self, key, value)
