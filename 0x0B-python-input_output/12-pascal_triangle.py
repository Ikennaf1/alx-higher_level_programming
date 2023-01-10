#!/usr/bin/python3

"""
A python module
"""


def pascal_triangle(n):
    """
    Returns the pascal's triangle
    """
    all_list = []
    prev_list = []
    curr_list = []
    left = 0
    right = 1
    val = 0
    x = 1
    width = x

    if n <= 0:
        return []
    while n > 0:
        left = 0
        right = 1
        width = x
        i = 0
        while width > 0:
            val = left + right
            curr_list.append(val)
            if len(prev_list) > 0:
                if 0 <= i and i < len(prev_list):
                    left = prev_list[i]
                if 0 <= (i + 1) and (i + 1) < len(prev_list):
                    right = prev_list[i + 1]
                else:
                    right = 0
            i += 1
            width -= 1
        all_list.append(curr_list)
        prev_list = curr_list.copy()
        curr_list = []
        n -= 1
        x += 1
    return all_list
