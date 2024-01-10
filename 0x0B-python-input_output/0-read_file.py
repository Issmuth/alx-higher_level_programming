#!/usr/bin/python3
"""Function that reads a file"""


def read_file(filename=""):
    """Reads a text file and prints to stdout.

    Args:
        filename: name of the file to be read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")

