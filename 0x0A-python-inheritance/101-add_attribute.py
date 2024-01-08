#!/usr/bin/python3


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object whose attribute is increased
        att: The name of the attribute to added
        value: The value of the attribute added
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
