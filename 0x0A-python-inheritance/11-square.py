#!/usr/bin/python3

"""
A derived class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square derived from a rectangle
    """

    def __init__(self, size):
        """
        Sets and validates square sides

        Args:
            size: `int` size of square sides
        """
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        String substitution for the class
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
