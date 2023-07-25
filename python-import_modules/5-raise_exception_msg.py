def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as e:
        print("Name exception raised:", str(e))
