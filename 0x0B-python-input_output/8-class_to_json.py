#!/usr/bin/python3

"""
A python module
"""


def class_to_json(obj):
    """
    Returns json seralized attributes of an object instance of a class
    """
    return obj.__dict__
