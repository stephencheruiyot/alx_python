"""initialize a class square
"""
class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square's sides.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.size = size

# Test the Square class
if __name__ == "__main__":
    square = Square(5)
    print(f"Square size: {square.size}")"""