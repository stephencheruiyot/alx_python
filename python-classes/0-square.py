class Square:
    """
    This class represents a square defined by its size.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Constructor for Square class.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
