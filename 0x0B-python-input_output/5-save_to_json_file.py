#!/usr/bin/python3
"""Module for a function that saves a
python object in json file."""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object in json representation
    inside a json file.

    Args:
        my_obj: object to be converted
        filename: name of the json file created
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
