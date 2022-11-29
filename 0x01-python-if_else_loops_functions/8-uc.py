#!/usr/bin/python3
def uppercase(s):
    endline = ""
    if s == "":
        s = ""
    for i in range(0, len(s)):
        endline = "" if i < len(s) - 1 else "\n"
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            for j in range(97, 123):
                if j == ord(s[i]):
                    print("{:c}".format(j - 32), end=endline)
                    break
        else:
            print("{}".format(s[i]), end="" if i < len(s) - 1 else "\n")
