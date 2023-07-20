#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1

# Determine the message based on the last digit
message = "Last digit of {} is {} and is".format(number, last_digit)

if last_digit > 5:
    message += " greater than 5"
elif last_digit == 0:
    message += " 0"
else:
    message += " less than 6 and not 0"

# Print the message
print(message)




 