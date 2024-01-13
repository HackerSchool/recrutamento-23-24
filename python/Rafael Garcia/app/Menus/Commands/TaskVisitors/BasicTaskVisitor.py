from libIO.FormIO.FieldIO.BasicIO.BasicIO import BasicIO
from core.Taskmsys import Taskmsys
from core.Tasks.Task import Task

''' Responsible for the output of every core element, like tasks'''
class BasicTaskVisitor:
    def __init__(self) -> None:
        self.userIO = BasicIO()
        self.render = ""
        
    def rendered(self):
        temp: str = self.render
        self.clear()
        return temp
    
    def clear(self):
        self.render = ""
        
    ''' Stores the output of priting an entire task system and stores on a atribute'''
    def visit_task_system(self, tasksys: Taskmsys):
        tasks: dict = tasksys.get_tasks()
        for entry in tasks:
            task: Task = tasks[entry]
            self.userIO.addText(f"Title: {task.get_title()}", True)
            self.userIO.addText(f"Description: {task.get_description()}", False)
        self.render = self.userIO.texted()
        self.userIO.clear()
        return self.render
            