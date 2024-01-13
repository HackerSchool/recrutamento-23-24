from lib.Commands.Forms.Fields.Field import Field

''' Class representing what a string field should look like'''
class StringField(Field):
    def __init__(self, prompt: str = "") -> None:
        super().__init__(prompt)
        
    #Override
    def parse(self, string: str):
        super().set_value(string)
        return True
    
    #Override
    def accept(self, visitor):
        return visitor.parseStringField(self)