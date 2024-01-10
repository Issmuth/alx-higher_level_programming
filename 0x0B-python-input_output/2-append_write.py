#!/bin/usr/python3
"""module of a function that appends text to a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a file

    Args:
        filename: name of the file
        text: text to be appended
    Returns: number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
