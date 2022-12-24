#!/usr/bin/python3

"""

A module to div a matrix

"""


def matrix_divided(matrix, div):
    """
    Divides a matrix and returns a new matrix containing result

    Args:
        matrix: `list` of `list` of numbers. The given matrix
        div: `int, float` The denominator

    Returns:
        A new matrix with the results
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    width = len(matrix[0])
    new_matrix = []
    n = 0

    for eachlist in matrix:
        if type(eachlist) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not len(eachlist) == width:
            raise TypeError("Each row of the matrix must have the same size")
        if len(eachlist) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append([])
        for x in eachlist:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            a = round(x / div, 2)
            new_matrix[n].append(a)
        n += 1

    return new_matrix
