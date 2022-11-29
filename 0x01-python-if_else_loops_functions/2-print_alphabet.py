#!/usr/bin/python3
for i in range(97, 123):
    print("{:c}".format(i), end="" if i != 122 else "\n")
