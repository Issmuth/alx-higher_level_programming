#!/usr/bin/python3
"""Module for a function that creates
a python object from a json file."""
import json


def load_from_json_file(filename):
    """Creates a python object from a json file.

    Args:
        filename: name of the file
    Returns:
        the python object loaded from json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
