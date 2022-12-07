#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        for i in range(len(my_list)):
            if my_list[i] == search:
                new_list[i] = replace
                continue
            new_list[i] = my_list[i]
    return new_list
