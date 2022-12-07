#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dictionary = a_dictionary.copy()
        for x in range(len(new_dictionary)):
            new_dictionary[x] = new_dictionary[x] * 2
    return new_dictionary
