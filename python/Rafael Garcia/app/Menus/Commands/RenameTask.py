from lib.Commands.Forms.Form import Form
from app.Menus.Commands.TaskCommands import TaskCommands
from core.Taskmsys import Taskmsys
from app.Menus.Commands.FieldPrompts.FieldPrompts import FieldPrompts

''' Command executed when renaming a task'''
class RenameTask(TaskCommands):
    def __init__(self, title: str, prompt: str, system: Taskmsys, valid: bool = True) -> None:
        super().__init__(title, prompt, system, valid)
        self.add_string_field("old_title", FieldPrompts.request_rename_old_prompt)
        self.add_string_field("new_title", FieldPrompts.request_rename_new_prompt)
        
    #Overrride
    def execute(self):
        ''' Getting the necessary arguemtns for the command'''
        if self.fill_arguments():
            if self.system.rename_task(self.get_string_field("old_title"), self.get_string_field("new_title")):
                return True
            self.userIO.pop(f'Task <{self.get_string_field("old_title")}> does not exist -_-')
        return False