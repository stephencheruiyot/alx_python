"""
A class to remove the attribute
    
"""
class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [ attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
"""
    
A class BaseGeometry
"""
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    A base class for geometry-related operations.

    Methods
    -------
    area()
        Raises an Exception with the message "area() is not implemented."
    integer_validator(name, value)
        Validates the input value as an integer, raising appropriate exceptions if not valid.
    """
    """
    def a method that excludes __init_subclass__
    """
    def __dir__(cls):
        return [attribute for attribute in super.__dir__() if attribute != '__init_sublass__']

    def area(self):
        """
        Raises an Exception to indicate that the area() method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the input value as an integer.

        Parameters
        ----------
        name : str
            The name of the value being validated.
        value : int
            The value to be validated.

        Raises
        ------
        TypeError
            If the value is not an integer.
        ValueError
            If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
