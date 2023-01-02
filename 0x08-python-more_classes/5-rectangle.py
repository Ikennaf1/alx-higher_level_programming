#!/usr/bin/python3

"""

A module for the rectangle class

"""


class Rectangle:
    """
    A rectangle class that sets width and height
    """

    def __init__(self, width=0, height=0):
        """
        `obj`: width and height of rectangle

        Args:
            width: `int` value of rectangle width
            height: `int` value of rectangle height
        Returns:
            `int`: size of width
        Raises:
            TypeError if width is not an integer
            ValueError: if width is negative
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        `obj`: width of rectangle

        Args:
            value: `int` value of rectangle width
        Returns:
            `int`: size of width
        Raises:
            TypeError if width is not an integer
            ValueError: if width is negative
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        `obj`: height of rectangle

        Args:
            value: `int` value of rectangle height
        Returns:
            `int`: size of height
        Raises:
            TypeError if height is not an integer
            ValueError: if height is negative
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """

        Returns the are of rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """

        Returns the perimeter

        """
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return perimeter
        return (self.__width + self.__height) * 2

    def __str__(self):
        """

        Provides string representation of the rectangle class

        """
        rect = ''
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rect += '#'
            rect += '\n' if i < self.__height - 1 else ''
        return rect

    def __repr__(self):
        """

        Returns representation of rectangle

        """

        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        """

        Detects instance deletion

        """
        print("Bye rectangle...")
