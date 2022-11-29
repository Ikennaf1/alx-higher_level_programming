#!/usr/bin/python3
def pow(a, b):
    temp = None
    if b == 0:
        return 1
    if b < 0:
        a = 1 / a
        b *= -1
    temp = a
    while b > 1:
        a *= temp
        b -= 1
    return a
