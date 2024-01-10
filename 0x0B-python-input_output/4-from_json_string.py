#!/usr/bin/python3
"""module for a function that converts
a json format to a python format(object)."""
import json


def from_json_string(my_str):
    """Converts a json string to a python format(object).

    Args:
        my_str: json string to be converted
    Returns:
        python format of the json string
    """
    return json.loads(my_str)
