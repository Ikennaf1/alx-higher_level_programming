#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(0, 2):
        if len(tuple_a) != 2:
            tuple_a = list(tuple_a)
            tuple_a.append(0)
            tuple_a = tuple(tuple_a)
        if len(tuple_b) != 2:
            tuple_b = list(tuple_b)
            tuple_b.append(0)
            tuple_b = tuple(tuple_b)
        new_tuple.append(tuple_a[i] + tuple_b[i])
    new_tuple = tuple(new_tuple)
    return new_tuple
