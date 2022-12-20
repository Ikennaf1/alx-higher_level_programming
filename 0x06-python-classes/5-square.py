#!/usr/bin/python3

class Square:
    """ Square class with more oomph """

    def __init__(self, size=0):
        """__init__ Initializes things

        Args:
            size: (:obj: `int`, optional)

        Raises:
            TypeError: If type is not `int`

            ValueError: If size is negative
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """size Gets the size of the square

        Args:
            size: (:obj: `int`, optional)

        Raises:
            TypeError: If size is not an `int`

            ValueError: If size is negative
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area returns the square area

        Returns:
            int: The calculated area
        """
        return self._size ** 2

    def my_print(self):
        """my_print Prints a square with the square using # as paint """
        if self.__size == 0:
            print()
        else:
            x = self.__size
            while x > 0:
                y = self.__size
                while y > 0:
                    print("#", end="")
                    y -= 1
                print()
                x -= 1
