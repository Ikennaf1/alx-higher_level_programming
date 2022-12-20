#!/usr/bin/python3

"""Square Class

A square class that does a lot more

"""


class Square:

    def __init__(self, size=0):
        """__init__

        The __init__ method initializes the size value of the square.

        Args:
            size (:obj: `int`, optional): The size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        """size

        Returns:
            int: the size of square

        """
        return self.__size

    @size.setter
    def size(self, size):
        """size

        Sets the size of square

        Args:
            size (:obj: `int`, optional): Size of the square

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: if `size` is negative

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """area

        Returns:
            int: The current square area

        """
        return self.__size ** 2
