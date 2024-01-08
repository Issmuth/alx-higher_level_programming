#!/usr/bin/python3

def lookup(obj):
    """Returns a list of attributes and methods of an object.
    Args:
        obj: object to be looked-up

    Returns: a list of the object contents
    """
    return dir(obj)
