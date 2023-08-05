"""
  An empty class with no attributes 
  nor methods  
"""
class BaseGeometryMetaclass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
        

class BaseGeometry(metaclass=BaseGeometryMetaclass):
    
    """
    def a function __dir__ to get access to the super attributes
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
        
