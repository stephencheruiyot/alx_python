def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: None.")
        return None
    except TypeError:
        print("Error: Both inputs must be integers.")
        return None
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None
    finally:
        print("Inside result: {}".format(result))

    return result


