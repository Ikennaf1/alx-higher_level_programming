#!/usr/bin/python3

def max_integer(my_list=[]):
    maxnum = 0
    if len(my_list) == 0:
        return None
    maxnum = my_list[0]
    for i in my_list[1:]:
        if maxnum < my_list[i]:
            maxnum = my_list[i]
    return maxnum
maxint = max_integer([])
print(maxint)
