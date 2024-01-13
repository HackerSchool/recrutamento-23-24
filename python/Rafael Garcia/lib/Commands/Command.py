from lib.Commands.Forms.Form import Form
from abc import ABC, abstractmethod
from libIO.FormIO.FormFill import FormFill

''' Class giving the skeleton of what a command should look like '''
class Command(ABC):
    def __init__(self, title: str, prompt: str, valid: bool=True, formulario: Form = None) -> None:
        self.valid = valid
        self.title = title
        self.prompt = prompt
        self.formulario = formulario
        self.form_filler = FormFill()
        
    def get_title(self):
        return self.title
    
    def is_valid(self):
        return self.valid
    
    def set_valid(self, boolean):
        self.valid = boolean
        
    def get_system(self):
        return self.system
    
    def get_prompt(self):
        return self.prompt
    
    def get_forms(self):
        return self.formulario
    
    
    ''' Every add <type> field adds an arguemnt of type <type> to be filled when calling the command
        given a certein prompt'''
    
    def add_string_field(self, key: str, prompt: str):
        return self.formulario.add_string_field(key, prompt)
    
    def add_boolean_field(self, key: str, prompt: str):
        return self.formulario.add_boolean_field(key, prompt)
    
    def add_time_field(self, key: str, prompt: str):
        return self.formulario.add_time_field(key, prompt)
    
    def get_string_field(self, key: str):
        return self.formulario.get_string_field(key)
    
    def get_boolean_field(self, key: str):
        return self.formulario.get_boolean_field(key)

    def get_time_field(self, key: str):
        return self.formulario.get_time_field(key)
    
    def fill_arguments(self):
        return self.form_filler.fill_form(self.formulario)
        
    @abstractmethod
    def execute(self):
        pass