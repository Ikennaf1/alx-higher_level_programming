#!/usr/bin/python3

"""
A Derived Class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle derived from geometry
    """
    def __init__(self, width, height):
        """
        Sets and validates Rectangle

        Args:
            width: `int` width of rectangle
            height: `int` Height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
