from lib.Commands.Forms.Fields.Field import Field

''' Class representing what a due time field should look like'''
class TimeField(Field):
    def __init__(self, prompt: str = "") -> None:
        super().__init__(prompt)
        
    #Override
    def parse(self, string: str):
        if len(string) == 9:
            try:
                [int(x) for x in string.split("/")]
                return True
            except Exception:
                return False
        return False
    
    #Override
    def accept(self, visitor):
        return visitor.parseTimeField(self)