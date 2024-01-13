""" Definição de algumas frases para não spamar no código """
class Prompts():
    pedirNome = "Nome da task: "
    novoNome = "Novo nome para a task: "
    novaDescricao = "Nova descricao para a task: "

    #Se quiseres adicionar operações também tens de mexer na classe Menu
    pedirMenuPrincipal = "1 - Adicionar Task\n\
2 - Remover Task\n\
3 - Ver Tasks\n\
4 - Editar Task Existente\n\
5 - Sair: \n"

    #Se quiseres adicionar operações também tens de mexer na classe Menu
    pedirMenu = "1 - Mudar nome\n\
2 - Muder descrição\n\
3 - Mudar ambos\n\
4 - Sair: \n"

    existeTask = "Task já existe"


""" Definição de uma task

### Atributos ###
name -> nome da task
description -> descrição da task

 """
class Task():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description
    
    def __str__(self):
        return "Task Name: " + self.name + " | Task Description: " + self.description
    

""" Classe que armazena todas as tasks

### Atributos ###
taskList -> dicionário que armazena as tasks, onde a key é
            o nome da task e o value a própria task

 """
class TaskList(Task):
    def __init__(self):
        self.taskList = {}
    
    def getTaskList(self):
        return self.taskList
    
    def setTaskList(self, taskList):
        self.taskList = taskList
    
    def getTask(self, taskName):
        return self.getTaskList().get(taskName)
    
    def taskAlreadyExists(self, taskName):
        if(taskName in self.getTaskList()):
            return True
        return False

    def addTask(self, task):
        if(self.taskAlreadyExists(task.getName())):
            print("\nImpossível criar task: Já existe uma task com este nome\n")
        else:
            self.taskList[task.name] = task
    
    def removeTask(self, taskName):
        if(self.taskAlreadyExists(taskName)):
            self.taskList.pop(taskName)
        else:
            print("\nImpossível remover task: Não existe uma task com este nome\n")
    

""" Classe onde são definidos os vários menus
 """
class Menu(Prompts):
    def menuPrincipal(self, taskList):
        operacao = -1
        while(operacao == -1):
            operacao = int(input(self.pedirMenuPrincipal))
            if(operacao == 1):
                op = AddTask()
            elif(operacao == 2):
                op = RemoveTask()
            elif(operacao == 3):
                op = InspectTasks()
            elif(operacao == 4):
                op = MenuChangeTask()
            elif(operacao == 5):
                return 0
            else:
                print("Operação inválida")
                operacao = -1

        if(op.execute(taskList) == 0):
            return 0
    
    
    def menuChangeTask(self, taskName, taskList):
        operacao = -1
        while(operacao == -1):
            operacao = int(input(self.pedirMenu))
            if(operacao == 1):
                op = ChangeName()
            elif(operacao == 2):
                op = ChangeDescription()
            elif(operacao == 3):
                op = ChangeNameAndDescription()
            elif(operacao == 4):
                return 0
            else:
                print("Operação inválida")
                operacao = -1

        if(op.execute(taskName, taskList) == 0):
            return 0


""" Classe que realiza a operação de adicionar tasks
 """
class AddTask(Prompts):
    def execute(self, taskList):
        taskName = input(self.novoNome)
        if(taskList.taskAlreadyExists(taskName)):
            print("\nImpossível criar task: Já existe uma task com este nome\n")
            return
        taskDescription = input(self.novaDescricao)
        taskList.addTask(Task(taskName, taskDescription))


""" Classe que realiza a operação de remover tasks
 """
class RemoveTask(Prompts):
    def execute(self, taskList):
        taskName = input(self.pedirNome)
        taskList.removeTask(taskName)


""" Classe que realiza a operação de ver as tasks
 """
class InspectTasks():
    def execute(self, taskList):
        values = taskList.getTaskList().values()
        if not values:
            print("Não há tasks :(")
        for tasks in values:
            print(tasks)


""" Classe que realiza a operação de abrir o menu de edição de tasks
 """
class MenuChangeTask(Menu):
    def execute(self, taskList):
        taskName = input(self.pedirNome)
        task = taskList.getTask(taskName)
        if(task != None):
            return self.menuChangeTask(taskName, taskList)  
        else:
            print("Nome inválido")


""" Classe que realiza a operação de mudar o nome de uma task
 """
class ChangeName(Prompts):
    def execute(self, taskName, taskList):
        task = taskList.getTask(taskName)
        task.setName(input(self.novoNome))


""" Classe que realiza a operação de mudar a descrição de uma task
 """
class ChangeDescription(Prompts):
    def execute(self, taskName, taskList):
        task = taskList.getTask(taskName)
        task.setDescription(input(self.novaDescricao))
            
    
""" Classe que realiza a operação de mudar o nome e a descrição de uma task
 """
class ChangeNameAndDescription(Prompts):
    def execute(self, taskName, taskList):
        task = taskList.getTask(taskName)
        task.setName(input(self.novoNome))
        task.setDescription(input(self.novaDescricao))



# Inicialização da lista de tasks
taskList = TaskList()
menu = Menu()

# Inicialização do menu principal
while(menu.menuPrincipal(taskList) != 0): 
    continue







        

