from lib.Commands.Forms.Form import Form
from app.Menus.Commands.TaskCommands import TaskCommands
from core.Taskmsys import Taskmsys
from app.Menus.Commands.FieldPrompts.FieldPrompts import FieldPrompts

''' Task executed when removing a task'''
class RemoveTask(TaskCommands):
    def __init__(self, title: str, prompt: str, system: Taskmsys, valid: bool = True) -> None:
        super().__init__(title, prompt, system, valid)
        self.add_string_field("title", FieldPrompts.request_remove_prompt)
        
    #Overrride
    def execute(self):
        ''' Getting the arguments for the commands '''
        if self.fill_arguments():
            if self.system.remove_task(self.get_string_field("title")):
                return True
            self.userIO.pop(f'Error Removing New Task: Task <{self.get_string_field("title")}> does not exist!')
        return False