#!/usr/bin/python3

"""
A geometry class
"""


class BaseGeometry:
    """
    A base geometry class that raises an exception
    """

    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")
