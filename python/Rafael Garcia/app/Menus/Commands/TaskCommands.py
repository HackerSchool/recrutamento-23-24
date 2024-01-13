from lib.Commands.Command import Command
from core.Taskmsys import Taskmsys
from lib.Commands.Forms.Form import Form
from libIO.FormIO.FieldIO.BasicIO.BasicIO import BasicIO

''' Class defining the skeleton of a command working on tasks'''
class TaskCommands(Command):
    def __init__(self, title: str, prompt: str, system: Taskmsys, valid: bool = True, formulario: Form = None) -> None:
        super().__init__(title, prompt, valid, formulario or Form())
        self.system = system
        self.userIO = BasicIO()
        
    def get_system(self):
        return self.system
    
    #Overrride
    def execute(self):
        pass