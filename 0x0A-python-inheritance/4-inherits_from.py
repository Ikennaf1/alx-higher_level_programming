#!/usr/bin/python3
"""
Method InheritsFrom
"""


def inherits_from(obj, a_class):
    """
    Checks if object obj inherits from class a_class

    Args:
        obj: The given object
        a_class: The given class

    Returns:
        `bool`: `True` or `False`
    """
    if isinstance(obj, a_class) and not issubclass(a_class, obj.__class__):
        return True

    return False
