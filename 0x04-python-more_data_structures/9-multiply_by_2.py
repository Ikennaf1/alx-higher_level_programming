#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dictionary = []
        for x in range(len(a_dictionary)):
            new_dictionary.append(a_dictionary[x] * 2)
    return new_dictionary
