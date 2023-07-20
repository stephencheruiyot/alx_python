#Write a function that computes a to the power of b and return the value.
def pow(a, b):
    result = 1

    # For positive or zero exponents
    if b >= 0:
        for _ in range(b):
            result *= a

    # For negative exponents
    else:
        for _ in range(-b):
            result /= a

    return result




