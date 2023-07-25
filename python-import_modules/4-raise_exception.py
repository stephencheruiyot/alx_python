def raise_exception():
    x = "This is a string, not a number"
    if not isinstance(x, int):
        raise TypeError("Expected an integer, but got a string.")
