#!/usr/bin/python3

def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and not issubclass(a_class, obj.__class__):
        return True

    return False
