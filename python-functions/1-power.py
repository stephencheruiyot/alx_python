def pow(a, b):
    if b == 0:
        return 1
    
    result = a
    for _ in range(1, abs(b)):
        result *= a
    
    if b < 0:
        result = 1 / result
    
    return result


