#!/usr/bin/python3
"""Module for a function that converts the dictionary description of a class."""


def class_to_json(obj):
    """Returns the dictionary description of a class.

    Args:
        obj: instance of the class to be described
    Returns:
        dictionary with simple data structure description
    """
    return obj.__dict__
