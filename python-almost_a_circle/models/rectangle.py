"""
rectangle.py - contains the class Rectangle that inherits from Base class   
"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base.

    Private instance attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    __x (int): The x-coordinate of the rectangle's position.
    __y (int): The y-coordinate of the rectangle's position.

    Public getter and setter properties:
    width (int): Get or set the width of the rectangle.
    height (int): Get or set the height of the rectangle.
    x (int): Get or set the x-coordinate of the rectangle's position.
    y (int): Get or set the y-coordinate of the rectangle's position.

    Class constructor:
    __init__(self, width, height, x=0, y=0, id=None):
        Initialize the Rectangle object with provided dimensions and position.

    Arguments:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
    y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
    id (int, optional): The ID of the rectangle. If not provided, it will be set by the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object with provided dimensions and position."""
        super().__init__(id)  # Call superclass constructor first
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: Getter for the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x variable"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Getter for the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y co-ordinate"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self,*args, **kwargs):
        '''Update the values of the Rectangle class
        
        Args:
             *args: Variable number of arguments for updating the attributes in the order:
                    id, width, height, x, y.
        kwargs: Keyword arguments for updating the attributes. Allowed keys are 'id', 'width', 'height', 'x', and 'y'.
        
        '''
        attrs = ['id','width','height','x', 'y']
        #update using positional arguments
        for idx, arg in enumerate(args):
            setattr(self,attrs[idx],arg)
            
        #update using keyword arguments
        for key, value in kwargs.items(): 
            if key in attrs:
                setattr(self, key, value)
        
            
        
       



               