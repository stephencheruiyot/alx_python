"""
square.py - contains the class Square that inherits from Rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Class constructor:
    __init__(self, size, x=0, y=0, id=None):
        Initialize the Square object with provided size and position.

    Arguments:
    size (int): The size of the square's sides.
    x (int, optional): The x-coordinate of the square's position. Defaults to 0.
    y (int, optional): The y-coordinate of the square's position. Defaults to 0.
    id (int, optional): The ID of the square. If not provided, it will be set by the Base class.
    """
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square object with provided size and position."""
        super().__init__(size, size, x, y, id)  # Call superclass constructor with width and height as size

    @property
    def size(self):
        """int: Getter for the size of the square's sides."""
        return self.width  # Size of square is same as width and height

    @size.setter
    def size(self, value):
        """Setter for the size of the square's sides."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''Update the values of the Square class
        
        Args:
             *args: Variable number of arguments for updating the attributes in the order:
                    id, size, x, y.
        kwargs: Keyword arguments for updating the attributes. Allowed keys are 'id', 'size', 'x', and 'y'.
        '''
        attrs = ['id', 'size', 'x', 'y']
        # Update using positional arguments
        for idx, arg in enumerate(args):
            setattr(self, attrs[idx], arg)
        
        # Update using keyword arguments
        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)
