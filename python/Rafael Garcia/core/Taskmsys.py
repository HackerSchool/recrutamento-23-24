from core.Tasks.Task import Task

''' Core Class responsible for managing tasks'''
class Taskmsys:
    def __init__(self, title: str="", tasks: dict={}) -> None:
        self.title = title
        self.tasks = tasks
        
    def get_tasks(self):
        return self.tasks
    
    def empty(self):
        return self.tasks == {}
        
    def create_task(self, title, description):
        if title in self.tasks:
            return False
        new_task = Task(title, description)
        self.tasks[title] = new_task
        return True
    
    def remove_task(self, title):
        if not self.tasks.pop(title, False):
            return False
        return True
    
    def rename_task(self, old_title, title):
        if old_title in self.tasks:
            task: Task = self.tasks[old_title]
            task.set_title(title)
            self.tasks[title] = self.tasks.pop(old_title)
            return True
        return False
    
    ''' Passes herself to a visitor which is going to store the string of priting her '''
    def accept(self, visitor):
        return visitor.visit_task_system(self)