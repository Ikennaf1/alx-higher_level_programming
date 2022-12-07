#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        my_set = set(my_list)
        uniq_sum = 0
        for i in my_set:
            uniq_sum += i
    return uniq_sum
