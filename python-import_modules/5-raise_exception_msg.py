def raise_exception_msg(message="C is fun"):
    class NameException(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    raise NameException(C is fun)

