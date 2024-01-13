from lib.Commands.Forms.Form import Form
from app.Menus.Commands.TaskCommands import TaskCommands
from core.Taskmsys import Taskmsys
from app.Menus.Commands.TaskVisitors.BasicTaskVisitor import BasicTaskVisitor

''' Command executed to list all tasks'''
class ListTask(TaskCommands):
    def __init__(self, title: str, prompt: str, system: Taskmsys, valid: bool = True) -> None:
        super().__init__(title, prompt, system, valid)
        self.taskVisitor = BasicTaskVisitor()
        
    #Overrride
    def execute(self):
        ''' Checks if there's tasks'''
        if not self.system.empty():
            ''' If there's is the output of this program is depended on the visitor '''
            text = self.system.accept(self.taskVisitor)
            if text:
                self.userIO.pop(text)
                self.taskVisitor.clear()
                return True
        self.userIO.pop(f"There's no task to list, create a task first!")
        return False