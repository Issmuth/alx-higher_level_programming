#!/usr/bin/python3
"""Module of a function that writes a text to a file"""


def write_file(filename="", text=""):
    """Writes a text to a file, overwrites if it exists,
    creates if it doesn't.

    Args:
        filename: name of the file
        text: text to write to the file
    Returns: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
       return  f.write(text)
