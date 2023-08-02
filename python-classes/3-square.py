"""
a class representing a square 
"""

class Square:
    
    """
    Attributes:
        size (int): The size of the square's side.
        
    constructor method: __init__(self, size=0)
    to initialize the value of side length to zero
    
    """
    def __init__(self, size=0):
        
        
        """
        private instance variable for storing the side length
        """
                
        """
        The @property decorator 
        defines a getter method for the "size" attribute.
        """
    @property
    def size(self):
        
        """
        Getter function that returns the current value

        Returns:
            __size: 
        """
        return self.__size
    
        """
        Setter Function:
        The @size.setter decorator defines a setter method
        for the "size" attribute.
        """
    @size.setter
    def size(self, size):
        
        """
        Sets new values for Side Length.
        Raises ValueError if input =< 0.
        """
                
        """size must be an integer, 
        otherwise raise a TypeError exception with the 
        message 'size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        
        """
        Raise valueError if size is less than zero
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
        """
        calculate the area of square:
        
        """
    def area(self):
        """Return:
        Area (side * side) using property method."""
        return self.__size ** 2