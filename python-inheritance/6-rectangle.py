"""
base class BaseGeometry
"""

class BaseGeometry:
    """
    base class BaseGeometry
    """

    
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter() method")

"""
sub class Rectangle
"""
class Rectangle(BaseGeometry):
    """
    sub class Rectangle
    """
    
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with width and height.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        ValueError: If width or height is not a positive integer.
        """
        self.__width = self.__height = None
        self.integer_validator(width, "width")
        self.integer_validator(height, "height")
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def integer_validator(self, value, name):
        """
        Validate if the value is a positive integer.

        Parameters:
        value (int): The value to be validated.
        name (str): The name of the value (used for error message).

        Raises:
        TypeError: must be an integer
        ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer.".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
