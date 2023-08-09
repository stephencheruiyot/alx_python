# square.py - contains the class Square that inherits from Rectangle

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Class constructor:
    __init__(self, size, x=0, y=0, id=None):
        Initialize the Square object with provided size and position.

    Arguments:
    size (int): The size of the square (both width and height).
    x (int, optional): The x-coordinate of the square's position. Defaults to 0.
    y (int, optional): The y-coordinate of the square's position. Defaults to 0.
    id (int, optional): The ID of the square. If not provided, it will be set by the Base class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square object with provided size and position."""
        super().__init__(size,size, x, y, id)  # Call superclass constructor with size for both width and height

    @property
    def size(self):
        """int: Getter for the size of the square."""
        return self.width  # Size is the same as width for a square

    @size.setter
    def size(self, value):
        """setter for size attribute"""
        self.width = value
        self.height = value  # Update both width and height with the same value

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
