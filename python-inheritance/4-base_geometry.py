"""
   A class BaseGeometry 

Raises:
        Exception:  area() is not implemented
"""

from collections.abc import Iterable


class BaseGeometry:
    """Base class for geometrical shapes."""
    def __dir__(cls):
        return [ attribute for attribute in super().__dir__() != '__init_subclass__']
        
    def area(self):
        """Calculate the area of the geometrical shape.
        
        This method should be implemented in the subclass.
        """
        raise Exception("area() is not implemented")
