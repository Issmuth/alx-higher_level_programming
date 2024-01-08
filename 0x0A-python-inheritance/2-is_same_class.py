#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class.

    Args:
        obj: object to be checked
        class: class to check against
    Returns: True if it's an instance False otherwise
    """
    if type(obj) is a_class:
        return True

    return False
