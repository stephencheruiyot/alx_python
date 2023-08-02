"""
A class Square that defines a square by: 

Private instance attribute: size   

"""

class Square:
    def __init__(self, size=0):
        """
        Constructor method to initialize the square's side length.

        Parameters:
            size (int): The size of the square's side. Default is 0.
        """
        self.__size = size
        
        """
        Getter method to return the current value of the side lenght.
        """

    def get_size(self):
        """
        Getter method that returns the current value of the side length.

        Returns:
            int: The current value of the side length.
        """
        return self.__size
        """
                Setter method to set the new value for the side lenght
        """

    def set_size(self, size):
        """
        Setter method to set a new value for the side length.

        Parameters:
            size (int): The new value for the side length.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
        """
        Area method  to calculate the area of a square
        """

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (side * side).
        """
        return self.__size * self.__size
