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
        Constructor to initialize the value of the side length.
        
        Args:
            size (int): The size of the square's side.

        """
        self.__size =size        
        """
        The @property decorator 
        defines a getter method for the "size" attribute.
        """
    @property
    def size(self):
        
        """
        Getter function that returns the current value

        Returns:
            int: The size of the square's side. 
        """
        return self.__size
    
        """
        Setter Function:
        The @size.setter decorator defines a setter method
        for the "size" attribute.
        """
    @size.setter
    def size(self, value):
        
        """
        Sets new values for Side Length.
        
        Args:
            Value (int) : New Size of the square's side.
        Raises:
            TypeError: If input is not an integer.
            ValueError if input =< 0.
        """
                
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value
        
    def area(self):
        """
        Return:
        Area (side * side) using property method.
        """
        return self.__size ** 2
    
    def my_print(self):
        if self.size ==0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)   