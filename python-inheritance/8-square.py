"""
A class BaseGeometry

"""

class BaseGeometry:
    def area(self):
        """
        This method must be implemented by subclasses to calculate the area.
        """
        raise NotImplementedError("Subclasses must implement this method.")

        """
        A class Rectangle
        argument:BaseGeometry

        
        """
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.
        :param width: Width of the rectangle
        :param height: Height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        :return: Area of the rectangle
        """
        return self.width * self.height
        """
       A class Square
       Arguments:Rectangle

        
        """

class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a square with the given size.
        :param size: Size of the square
        """
        # Validate the input size
        self.integer_validator(size)
        # Call the constructor of the parent class (Rectangle)
        super().__init__(size, size)

    @staticmethod
    def integer_validator(value):
        """
        Validates that the given value is a positive integer.
        :param value: Value to be validated
        :raises ValueError: If the value is not a positive integer
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Size must be a positive integer.")

