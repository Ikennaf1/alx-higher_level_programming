#!/usr/bin/python3

"""
A Derived class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square derived from rectangle
    """

    def __init__(self, size):
        """
        Sets and validates square dimensions

        Args:
            size: `int` the size of square sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
