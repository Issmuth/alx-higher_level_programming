#!/usr/bin/python3
"""Module for a function that converts 
an object(string) to json string."""
import json


def to_json_string(my_obj):
    """Shows the string representation of an
    object or string in json.

    Args:
        my_obj: object to be converted
    Returns:
        converted json format
    """
    return json.dumps(my_obj)
