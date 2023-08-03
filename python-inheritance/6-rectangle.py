"""
 initialize base class   
    
"""

class BaseGeometry:
    """
    Base class for geometrical shapes.

    Methods:
        area(): Abstract method to calculate the area of the shape.
    """

    def area(self):
        """
        Calculate the area of the shape.
        This is an abstract method and should be implemented in the subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")

"""
 Rectangle class       

"""
class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry.

    Attributes:
        __width (int): Private attribute representing the width of the rectangle.
        __height (int): Private attribute representing the height of the rectangle.

    Methods:
        __init__(self, width, height): Constructor method for Rectangle.
    """

    def __init__(self, width, height):
        """
        Constructor for Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator(width, height,int)
        self.__width = width
        self.__height = height

    def integer_validator(self, width, height):
        """
        Validate if width and height are positive integers.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("{} must be an integer".format(height,width))
        if width <= 0 or height <= 0:
            raise ValueError("{} must be an integer".format(height, width))

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
