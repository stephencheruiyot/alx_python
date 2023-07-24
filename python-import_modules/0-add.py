a = 1
b = 2

if __name__ == "__main__":
    from add_0 import add

    result = add(a, b)
    print("{a} + {b} = {result}".format(a, b, a + b))
