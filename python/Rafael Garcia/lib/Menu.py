from lib.Commands.Command import Command
from abc import ABC, abstractmethod

''' Class giving the skeleton of what a menu should look like '''
class Menu(ABC):
    def __init__(self, title: str, commands: list=[]) -> None:
        self.title: str = title
        self.commands: list = commands
        
    def get_title(self) -> str:
        return self.title
    
    def get_commands(self):
        return self.commands
    
    def get_command(self, i: int):
        return self.commands[i]
    
    def size(self):
        return len(self.commands)