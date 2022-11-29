#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if num < 0:
    num *= -1
last_digit = 0
comment = ""
last_digit = num % 10
if number < 0:
    last_digit *= -1
if last_digit > 5:
    comment = "greater than 5"
elif last_digit == 0:
    comment = "0"
elif last_digit < 6 and last_digit != 0:
    comment = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {comment}")
