def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Test cases
print(add(1, 2))    # Output: 3
print(add(98, 0))   # Output: 98
print(add(100, -2)) # Output: 98
