#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    endline = ""
    if matrix:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                endline = " " if j != len(matrix[i]) - 1 else "\n"
                print("{:d}".format(matrix[i][j]), end=endline)
    else:
        print()
