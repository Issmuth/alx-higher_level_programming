#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class
    less rigorously.

    Args:
        obj: object to be checked
        a_class: class to be checked against
    Returns: True if it's an instance False otherwise
    """
    if isinstance(obj, a_class):
        return True

    return False
