"""
 A class BaseGeometry   
    
"""

class BaseGeometry:
    """
    A class BaseGeometry
    """
    
    def area(self):
        """
        This method should be implemented by subclasses to calculate the area of a geometry.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
