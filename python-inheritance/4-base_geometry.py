"""
   A class BaseGeometry 

Raises:
        Exception:  area() is not implemented
"""

class BaseGeometry:
    """Base class for geometrical shapes."""

    def area(self):
        """Calculate the area of the geometrical shape.
        
        This method should be implemented in the subclass.
        """
        raise Exception("area() is not implemented")
