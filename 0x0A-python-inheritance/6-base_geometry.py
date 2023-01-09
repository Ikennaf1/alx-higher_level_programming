#!/usr/bin/python3

"""
A base Class
"""


class BaseGeometry:
    """
    A Geometry class that raises an exception
    """
    def area(self):
        raise Exception('area() is not implemented')
