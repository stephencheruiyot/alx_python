def raise_exception():
    try:
        # Attempt to raise a type exception
        raise TypeError("Exception has been raised.")
    except TypeError as e:
        # Catch the raised exception and print the error message
        print("Exception raised:", e)
