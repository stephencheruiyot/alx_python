"""
A class BaseGeometry
   
"""

class BaseGeometry:
    """
    Abstract base class representing geometric shapes with two sides 
    """
    def area(self):
        """
        Calculates the area of the geometry.

        Returns:
            float: The area of the geometry.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        """
        Calculates the perimeter of the geometry.

        Returns:
            float: The perimeter of the geometry.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def integer_validator(self, value, name):
        """
        Validates if the given value is a positive integer.

        Args:
            value (int): The value to be validated.
            name (str): The name of the value for error messages.

        Raises:
            TypeError: width must be an integer
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise TypeError(f"{name} must be an integer")
        
"""
Rectangle class that inherits from BaseGeometry.
"""
class Rectangle(BaseGeometry):
        
    """
Constructor for Rectangle instances.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator(width, "width")
        self.integer_validator(height, "height")

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
        """
        Method to calculate the perimeter of the rectangle.
        """

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)
