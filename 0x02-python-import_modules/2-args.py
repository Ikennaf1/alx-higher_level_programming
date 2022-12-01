#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argcount = len(sys.argv) - 1
    arglit = "argument" if argcount == 1 else "arguments"
    arglitappend = ":" if argcount > 0 else "."
    count = 1

    print("{:d} {}{}".format(argcount, arglit, arglitappend))

    if argcount > 0:
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(count, arg))
            count = count + 1
