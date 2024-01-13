from lib.Commands.Forms.Fields.Field import Field
''' Class representing what a Boolean field should look like'''
class BooleanField(Field):
    def __init__(self, prompt: str = "") -> None:
        super().__init__(prompt)
        
    #Override
    def parse(self, string: str):
        confirm = ["yes", "y"]
        negative = ["no", "n"]
        everything = confirm + negative
        
        if string in everything:
            if string in confirm:
                super().set_value(True)
            elif string in negative:
                super().set_value(False)
            return True
        return False
    
    #Override
    def accept(self, visitor):
        return visitor.parseBooleanField(self)