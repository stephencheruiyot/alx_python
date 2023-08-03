"""
   A function with two parameters
    
"""
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class 
    that inherited
    from the given class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to check inheritance from.

    Returns:
        True if the object is an instance of a class inherited from 'a_class', otherwise False.
    """
        
    classes = type(obj).mro()

    # Check if 'a_class' is in the set of classes the object belongs to
    return any(a_class is c for c in classes[1:])  
# Start from index 1 to skip the object's own class

