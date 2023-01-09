#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Returns true if given obj is exact
    Checks if `obj` is exactly an instance of the specified class
    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object
    Returns:
        `True` if the object is exactly an instance of the
        specified class; otherwise `False`
    """
    if type(obj) == a_class:
        return True
    return False
