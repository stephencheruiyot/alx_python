#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit of the number using the modulo operator (%)
last_digit = abs(number) % 10
# Print the output based on the last digit including a sign 
sign = "-" if number < 0 else ""
print(f"Last digit of {number} is {sign}{last_digit} and is")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")



 