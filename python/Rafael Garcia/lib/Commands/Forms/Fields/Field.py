from abc import ABC, abstractmethod

''' Class representing what a field looks like
    Stores a prompt and hold a atrivute value
    Parses a string and if it matches the field
    type in stores it in a value'''
class Field(ABC):
    def __init__(self, prompt: str= "") -> None:
        self.prompt = prompt
        self.value = None
    
    def get_prompt(self):
        return self.prompt
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
    @abstractmethod
    def parse(self, string: str):
        pass
    
    @abstractmethod
    def accept(self, visitor):
        pass