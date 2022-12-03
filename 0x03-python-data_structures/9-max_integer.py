#!/usr/bin/python3

def max_integer(my_list=[]):
    maxnum = 0
    if not my_list:
        return None
    maxnum = my_list[0]
    for i in my_list[1:]:
        if maxnum < my_list[i]:
            maxnum = i
    return maxnum
