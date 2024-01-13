from core.Tasks.Task import Task
import json

''' Class used for enconding task object into JSON object'''
class TaskDecoder(json.JSONDecoder):
    def decode(self, s):
        decoded_data = super().decode(s)
        tasks = {}

        for key, value in decoded_data.items():
            if 'title' in value and 'description' in value:
                tasks[key] = Task(value['title'], value['description'])

        return tasks