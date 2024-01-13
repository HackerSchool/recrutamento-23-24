from core.Tasks.Task import Task
import json

''' Class used for deconding JSON object into task object'''
class TaskEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Task):
            return {'title': obj.title, 'description': obj.description}
        return super().default(obj)
