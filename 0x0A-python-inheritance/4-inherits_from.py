#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Checks if object obj inherits from class a_class
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
