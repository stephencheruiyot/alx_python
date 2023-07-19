#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = (number) % 10
result_string = "Last digit of {} is {} ".format(number, last_digit)

if last_digit > 5:
    result_string += "and is greater than 5"
elif last_digit == 0:
    result_string += "and is 0"
else:
    result_string += "and is less than 6 and not 0"

print(result_string)

 