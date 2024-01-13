from typing import TextIO
import os
import json

promptsOptions = ["Q", "E", "D", "N"]


class Task:
    """
    A class to represent a task, containing a topic and a description
    """
    def __init__(self, topic: str, description: str) -> None:
        self.topic = topic
        self.description = description

    def __str__(self) -> str:
        return f'{self.topic}: {self.description}'


class User:
    """
    Class for the User calendar and it's methods.
    """

    def __init__(self) -> None:
        self.taskList = []
        self.planner_file = None

    def newTask(self) -> None:
        """
        Gets the user input and adds it as a task to our planner
        """
        topic = input('Enter topic: ')
        description = input('Enter description: ')
        self.addTask(Task(topic, description))

    def addTask(self, task: Task) -> None:
        """
        Method to add a task to our plannner
        """
        self.taskList.append(task)

    def exportCalendar(self) -> None:
        """
        Method that reads our current planner and exports it into a json file
        """
        data = {}
        for task_no, task in enumerate(self.taskList):
            data.update({task_no: {"topic": task.topic, "description": task.description}})
        self.planner_file.seek(0)
        json.dump(data, self.planner_file, indent=4)
        self.planner_file.truncate()

    def importCalendar(self) -> None:
        """
        Method that reads a json file and adds what was in it to our planner
        """
        data = json.load(self.planner_file)
        for task_no, task in data.items():
            self.addTask(Task(task["topic"], task["description"]))

    def editTask(self) -> None:
        """
        Shows off the list of current tasks and lets the user edit one of them by retyping the new topic and description
        """
        self.getTaskList()
        index = int(input('Which task do you wanna edit: '))
        topic = input('Enter new topic: ')
        description = input('Enter new description: ')
        self.deleteTask(index - 1)
        self.addTask(Task(topic, description))

    def deleteTask(self, index: int = -1) -> None:
        """
        Deletes a specified task from the planner
        """
        self.getTaskList()
        print(len(self.taskList))
        while index < 0 or index > len(self.taskList):
            index = int(input('Which task do you want to delete: '))
        self.taskList.pop(index - 1)

    def getTaskList(self) -> None:
        if len(self.taskList) == 0:
            print("You don't have any tasks planned")
        else:
            print(f'List of tasks:')
            for number, task in enumerate(self.taskList):
                print(f'{number + 1}. {task.topic}: {task.description}')

    def Quit(self):
        self.exportCalendar()
        self.planner_file.close()
        quit()

    def getInput(self) -> None:
        """
        Gets user input and validates with our options defined in a list of chars
        """
        option = ""
        while option not in promptsOptions:
            self.getTaskList()
            self.printOptionPrompt()
            option = input("").upper()
        if option == "E":
            if len(self.taskList) == 0:
                print("You don't have any tasks planned")
            else:
                self.editTask()
        if option == "N":
            self.newTask()
        if option == "D":
            if len(self.taskList) == 0:
                print("You don't have any tasks planned")
            else:
                self.deleteTask()
        if option == "Q":
            self.Quit()

    def printOptionPrompt(self) -> None:
        print(f'What would you like to do:\n(N)ew  (D)elete  (E)dit  (Q)uit\n')

    def openfile(self, filename: str = "planner.json") -> None:
        """
        Opens a json file with default name 'planner.json', if the file has text it opens in
        read and write mode importing what was inside. Otherwise it creates a file in a writable mode only
        """
        try:
            if os.stat(filename).st_size != 0:
                self.planner_file = open(filename, 'r+')
                self.importCalendar()
        except IOError:
            self.planner_file = open(filename, 'w')


def cls():
    """
    Simple function to clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    cls()
    user = User()
    user.openfile()
    while True:
        cls()
        user.getInput()


