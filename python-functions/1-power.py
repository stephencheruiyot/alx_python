def pow(a, b):
    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    while b:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result




