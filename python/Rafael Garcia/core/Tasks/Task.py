''' Class representing a task '''
class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description