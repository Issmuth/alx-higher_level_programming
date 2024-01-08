#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that is inherited from a specific class.

    Args:
        obj: object to be checked
        a_class: Superclass checked against
    Returns: True if inherited False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
