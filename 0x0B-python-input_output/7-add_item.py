#!/usr/bin/python3
"""A script that accepts arguments and adds
them into python list saved as a json file."""
import sys


if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = \
         __import__('5-save_to_json_file').save_to_json_file

    try:
        data = load_from_json_file("add_items.json")
    except FileNotFoundError:
        data = []

    data.extend(sys.argv[1:])
    save_to_json_file(data, "add_items.json")
