from app.Menus.CommandPrompts import CommandPrompts
from app.Menus.TaskMenu import TaskMenu
from core.Taskmsys import Taskmsys
from app.Menus.Commands.RenameTask import RenameTask
from app.Menus.Commands.ListTask import ListTask

''' Menu that is opened when we are going to edit a task '''
class EditMenu(TaskMenu):
    def __init__(self, title: str, system: Taskmsys, commands: list = []) -> None:
        if commands == []:
            commands.extend(
            [
                RenameTask("renomear", CommandPrompts.rename_prompt, system),
                ListTask("list", CommandPrompts.list_prompt, system)
            ]
            )
        super().__init__(title, system, commands)
        