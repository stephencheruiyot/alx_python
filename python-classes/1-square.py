"""
a class representing a square 
"""

class Square:
    
    """
    constructor method to initialize the value of side length to zero
    """
    def __init__(self, size=0):
        
        
        """
        private instance variable for storing the side length
        """
        self.__size = size
        
        """
        public getter and setter methods for accessing/modifying
        """
    def get_size(self):
        
        """
        Getter function that returns the current value

        Returns:
            _type_: _description_
        """
        return self.__size
    
        """
        Setter Function 
        """
    def set_size(self, size):
        
        """
        Sets new values for Side Length. Raises ValueError if input is less than or equal to zero.
        """
        self.__size = size
        
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