def add(a, b):
    # Use the bitwise operations to simulate addition
    while b != 0:
        carry = a & b  # calculate the common set bits (carry bits)
        a = a ^ b      # add bits of a and b without considering the carry
        b = carry << 1 # shift carry by one position to the left

    return a



