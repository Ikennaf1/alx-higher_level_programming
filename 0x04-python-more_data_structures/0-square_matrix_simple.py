#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = matrix.copy()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                new_matrix[row][col] *= new_matrix[row][col]
        return new_matrix
