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

    def area(self):
        """rectangle area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
