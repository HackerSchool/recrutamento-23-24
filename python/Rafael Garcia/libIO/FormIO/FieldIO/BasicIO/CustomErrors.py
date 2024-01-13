class EmptyString(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)
        
class NegativeNumber(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)
        
class IsNotNumber(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)
        
class InvalidNumber(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)