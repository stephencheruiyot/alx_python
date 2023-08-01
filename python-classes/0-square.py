class Square:
    """
    A class that defines a square by its size.

    Attributes:
        size (int): The size of the square (side length).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square (side length).
        """
        self._size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self._size

    def get_size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square (side length).
        """
        return self._size

    def set_size(self, new_size):
        """
        Set the size of the square to a new value.

        Args:
            new_size (int): The new size of the square (side length).
        """
        self._size = new_size
