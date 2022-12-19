#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    endline = ""
    try:
        for i in range(0, x):
            endline = "" if i < (x - 1) else "\n"
            print("{}".format(my_list[i]), end=endline)
    except (TypeError, IndexError):
        print()
        return i
    i += 1
    return i
