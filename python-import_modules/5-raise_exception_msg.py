def raise_exception_msg(message=""):
    class NameException(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    raise NameException(message)

