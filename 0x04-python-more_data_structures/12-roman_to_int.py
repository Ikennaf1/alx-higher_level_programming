#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        r_num = {
                'i': 1,     'I': 1,
                'v': 5,     'V': 5,
                'x': 10,    'X': 10,
                'l': 50,    'L': 50,
                'c': 100,   'C': 100,
                'd': 500,   'D': 500,
                'm': 1000,  'M': 1000
        }
        num = 0
        for i in range(len(roman_string)):
            if i < (len(roman_string) - 1):
                if r_num[roman_string[i + 1]] > r_num[roman_string[i]]:
                    num -= r_num[roman_string[i]]
                else:
                    num += r_num[roman_string[i]]
            else:
                num += r_num[roman_string[i]]
        return num
    else:
        return 0
