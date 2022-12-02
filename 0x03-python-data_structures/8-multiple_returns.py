#!/usr/bin/python3

def multiple_returns(sentence):
    my_tuple = [0, ""]
    strlen = len(sentence)
    char1 = sentence[0] if len(sentence) > 0 else None
    my_tuple[0] = strlen
    my_tuple[1] = char1
    my_tuple = tuple(my_tuple)
    return my_tuple
