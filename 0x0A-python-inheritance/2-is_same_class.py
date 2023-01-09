#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Returns true if given obj is instance of a_class class
    """
    if type(obj) == a_class:
        return True
    return False
