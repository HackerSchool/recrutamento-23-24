from lib.Commands.Forms.Fields.Field import Field
from lib.Commands.Forms.Fields.StringField import StringField
from lib.Commands.Forms.Fields.BooleanField import BooleanField
from lib.Commands.Forms.Fields.TimeField import TimeField

''' Class representing what a form for a command should look like
    It stores prompts that must be answered when the given comamnd
    with the given form is called '''
class Form:
    
    def __init__(self, title: str="", fields: dict=None) -> None:
        self.title = title
        self.fields = fields or {}
        
    def get_title(self):
        return self.title
    
    def add_field(self, key: str, field: Field):
        if key in self.fields:
            return False
        self.fields[key] = field
        
    ''' Adds a prompt and argument that must be answered when calling the  comamnd
        arguemnt has type -> add_<type>_field'''
    def add_string_field(self, key: str, prompt: str):
        return self.add_field(key, StringField(prompt))
    
    def add_boolean_field(self, key: str, prompt: str):
        return self.add_field(key, BooleanField(prompt))
    
    def add_time_field(self, key: str, prompt: str):
        return self.add_field(key, TimeField(prompt))
    
    def get_fields(self):
        return self.fields
    
    def get_field(self, key:str):
        if key in self.fields:
            field: Field = self.fields[key]
            return field.get_value()
        return None
    
    def get_string_field(self, key: str):
        return self.get_field(key)
    
    def get_boolean_field(self, key: str):
        return self.get_field(key)

    def get_time_field(self, key: str):
        return self.get_field(key)