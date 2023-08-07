"""
models.base - Contains the Base class for the Python Almost A Circle project.
"""

class Base:
    """
    Base class for the Python Almost A Circle project.

    Private class attribute:
        __nb_objects (int): Keeps track of the number of instances created.

    Public instance attributes:
        id (int): Unique identifier for each instance.

    Constructor:
        def __init__(self, id=None):
        Initializes a Base object.
        If id is not None, it will be assigned to the instance attribute 'id'.
        If id is None, __nb_objects will be incremented and assigned to 'id'.

        Parameters:
            id (int, optional): Unique identifier for the instance. Defaults to None.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        If id is not None, it will be assigned to the instance attribute 'id'.
        If id is None, __nb_objects will be incremented and assigned to 'id'.

        Parameters:
            id (int, optional): Unique identifier for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
