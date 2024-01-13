from app.Menus.CommandPrompts import CommandPrompts
from app.Menus.TaskMenu import TaskMenu
from core.Taskmsys import Taskmsys
from app.Menus.Commands.CreateTask import CreateTask
from app.Menus.Commands.RemoveTask import RemoveTask
from app.Menus.Commands.EditTask import EditTask
from app.Menus.Commands.ListTask import ListTask

''' Menu that is opened when we execute the program '''
class OpenMenu(TaskMenu):
    def __init__(self, title: str, system: Taskmsys, commands: list =[]) -> None:
        if commands == []:
            commands.extend(
            [
                CreateTask("create", CommandPrompts.create_prompt, system),
                RemoveTask("remove", CommandPrompts.remove_prompt, system),
                EditTask("edit", CommandPrompts.edit_prompt, system),
                ListTask("list", CommandPrompts.list_prompt, system)
            ]
            )
        super().__init__(title, system, commands)