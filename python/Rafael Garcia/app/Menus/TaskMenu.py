from app.Menus.CommandPrompts import CommandPrompts
from lib.Menu import Menu
from core.Taskmsys import Taskmsys

''' Class describing a task menu, based on the providing app '''
class TaskMenu(Menu):
    def __init__(self, title: str, system: Taskmsys, commands: list = None) -> None:
        super().__init__(title, commands or [])
        self.system = system