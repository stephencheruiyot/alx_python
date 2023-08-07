# models/rectangle.py
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

    Example:
    >>> rect = Rectangle(10, 5, 2, 3)
    >>> rect.width
    10
    >>> rect.height
    5
    >>> rect.x
    2
    >>> rect.y
    3
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object with provided dimensions and position."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """int: Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """int: Get or set the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """int: Get or set the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
