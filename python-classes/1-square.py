"""
a class representing a square 
"""

class Square:
    
    """
    constructor method to initialize the value of side length to zero
    """
    def __init__(self, size=0):
        
        
        """
        private instance variable 
        for storing the side length
        """
        
        """
        public getter and setter methods for accessing/modifying
        """
    def get_size(self):
        
        """
        Getter function that returns the current value

        Returns:
            self: _description_
        """
        
        """
        Setter Function 
        """
    def set_size(self, size):
        
                
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