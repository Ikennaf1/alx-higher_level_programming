#!/usr/bin/python3

"""Square Class

A square class that returns area

"""


class Square:
    """__init__

        The __init__ method initializes the size value
        of the square.

        Attributes:
            size (int): The size of the square.
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area

        The area method returns the area of the square.

        """
        area = self.__size * self.__size
        return area
