#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Checks if object is instance of a_class class
    """
    return isinstance(obj, a_class) and not issubclass(a_class, obj.__class__)
