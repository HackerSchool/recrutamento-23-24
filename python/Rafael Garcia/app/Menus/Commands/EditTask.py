from app.Menus.Commands.TaskCommands import TaskCommands
from core.Taskmsys import Taskmsys
from libIO.MenuOpener import MenuOpener
from app.Menus.EditMenu import EditMenu

''' Command executed when editing a task '''
class EditTask(TaskCommands):
    def __init__(self, title: str, prompt: str, system: Taskmsys, valid: bool = None) -> None:
        super().__init__(title, prompt, system, valid or True)
        self.menu_opener = MenuOpener()
        self.menu = EditMenu("edit", system, [])

    #Overrride
    def execute(self):
        ''' Opens the edit menu '''
        self.menu_opener.open_menu(self.menu)
        return True