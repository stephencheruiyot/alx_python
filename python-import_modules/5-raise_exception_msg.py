def raise_exception_msg(message=""):
    raise NameError(message)

# Test the function
try:
    raise_exception_msg("This is a custom name exception!")
except NameError as e:
    print("Caught the exception:", e)
