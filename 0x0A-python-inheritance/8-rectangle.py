#!/usr/bin/python3
"""
A subclass
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle derived from geometry
    """
    def __init__(self, width, height):
        """
        Sets and validates the dimensions

        Args:
            width: `int` width of rectangle
            height: `int` Height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
