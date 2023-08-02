"""initialize a class square
"""
class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square's sides.
    """

    """
    Initialize a square instance
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        
        """
        size must be an integer, 
        otherwise 
        raise a TypeError exception with the message
        size must be an integer
        
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        """
        if size is less than 0, 
        raise a ValueError exception with the message
        size must be >= 0
        
        """

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    