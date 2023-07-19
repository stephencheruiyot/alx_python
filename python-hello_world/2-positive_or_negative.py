#!/usr/bin/python3
import random
number = random.randint(-10, 10)


def random_sign():


    if number > 0:
        sign = "positive"
    elif number == 0:
        sign = "zero"
    else:
        sign = "negative"

    print(f"{number}: is {sign}")

if __name__ == "__main__":
    
    for _ in range(1):  # Replace 10 with the desired number of random numbers you want to generate.
        random_sign()


