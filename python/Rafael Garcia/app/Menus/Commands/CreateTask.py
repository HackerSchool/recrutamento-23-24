from app.Menus.Commands.TaskCommands import TaskCommands
from core.Taskmsys import Taskmsys
from app.Menus.Commands.FieldPrompts.FieldPrompts import FieldPrompts

''' Command executed when creating a task '''
class CreateTask(TaskCommands):
    def __init__(self, title: str, prompt: str, system: Taskmsys, valid: bool = True) -> None:
        super().__init__(title, prompt, system, valid)
        self.add_string_field("title", FieldPrompts.request_title_prompt)
        self.add_string_field("description", FieldPrompts.request_description_prompt)
        
    #Overrride
    def execute(self):
        ''' Getting the arguemtns needed for the command '''
        if self.fill_arguments():
            if self.system.create_task(self.get_string_field("title"), self.get_string_field("description")):
                return True
            self.userIO.pop(f'Error Creating New Task: Task <{self.get_string_field("title")}> already exists!')
        return False