"""
A function that has an object and the 
specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of, or if it is an instance of a class
    that inherited from the specified class.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The specified class or its subclass to compare with.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass,
              otherwise False.
    """
    return isinstance(obj, a_class)
