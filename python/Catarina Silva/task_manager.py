# Define a class 'Task' to represent a task with a task_id, name, and description
class Task:
    def __init__(self, task_id, name, desc):
        self.task_id = task_id
        self.name = name
        self.desc = desc

# Main loop for task management
while 1:
    # Display menu options
    print("O que é que queres fazer hoje? Pressiona a tecla correspondente")
    print("1 - adicionar uma tarefa")
    print("2 - editar uma tarefa")
    print("3 - apagar uma tarefa")
    print("4 - ver as tarefas")
    print("0 - sair")

    # Get user input for selected option
    option = int(input())

    # Validate the selected option
    if option > 4 or option < 0:
        print("Essa opção não é válida, tenta de novo")
    else:
        # Option to add a new task
        if option == 1:
            name = input("Dá um nome à tua tarefa: ")
            desc = input("Escreve uma descrição sobre o que tens de fazer: ")
            # Open 'tasks.txt' in append mode, write task details, and close the file
            f = open("tasks.txt", "a")
            f.write(" \n")
            f.write(name + " - " + desc)
            f.close()
            print("Tarefa guardada com sucesso :D\n")

        # Option to edit an existing task
        elif option == 2:
            # Initialize an empty dictionary to store tasks
            task_list = {}
            print("Seleciona a tarefa que queres editar: ")
            # Read lines from 'tasks.txt' and create Task objects with task_id, name, and desc
            f = open("tasks.txt", "r").readlines()
            task_id = 1

            for line in f:
                if line.strip():
                    row = line.split('-')
                    name, desc = [i.strip() for i in row]
                    task_list[task_id] = Task(task_id, name, desc)
                    task_id += 1
            
            counter = 0
            # Display tasks and their IDs for selection
            for each_key in task_list:
                print(each_key, " - ", task_list[each_key].name)
                counter += 1
            print("0 - cancelar")

            # Get user input for the task to edit
            id = int(input())

            # Validate the selected task ID
            if id > 0 and id <= counter:
                # Prompt user for editing options
                print("Queres editar o nome e/ou a descrição?")
                print("1 - nome")
                print("2 - descrição")
                print("3 - os dois")

                # Get user input for editing option
                option = int(input())

                # Perform the selected edit operation
                if option == 1:
                    task_list[id].name = input("Dá um novo nome à tua tarefa: ")
                    print("Gostei do novo nome. Ficou guardado ;)\n")
                elif option == 2:
                    task_list[id].desc = input("Escreve uma nova descrição sobre o que tens de fazer: ")
                    print("Adorei saber mais sobre o que vais fazer. Vou guardar!\n")
                elif option == 3:
                    task_list[id].name = input("Dá um novo nome à tua tarefa: ")
                    task_list[id].desc = input("Escreve uma nova descrição sobre o que tens de fazer: ")
                    print("Senti essa indecisão sobre a tua tarefa mas isso não me vai impedir de a guardar :)\n")
                else:
                    print("Essa não é uma opção válida! Tenta de novo\n")

                # Write the updated tasks to 'tasks.txt'
                with open("tasks.txt", "w") as f:
                    for each_key in task_list:
                        f.write(task_list[each_key].name + " - " + task_list[each_key].desc + "\n")

            elif id != 0:
                print("Não consegui encontrar a tua tarefa. Talvez me tenha esquecido dela...\n") 

        # Option to delete a task
        elif option == 3:
            # Initialize an empty dictionary to store tasks
            task_list = {}
            print("Seleciona a tarefa que queres apagar: ")
            # Read lines from 'tasks.txt' and create Task objects with task_id, name, and desc
            f = open("tasks.txt", "r").readlines()
            task_id = 1
            
            for line in f:
                if line.strip():
                    row = line.split('-')
                    name, desc = [i.strip() for i in row]
                    task_list[task_id] = Task(task_id, name, desc)
                    task_id += 1

            counter = 0
            # Display tasks and their IDs for selection
            for each_key in task_list:
                print(each_key, " - ", task_list[each_key].name)
                counter += 1
            print("0 - cancelar")

            # Get user input for the task to delete
            id = int(input())

            # Validate the selected task ID
            if id > 0 and id <= counter:
                # Remove the selected task from the dictionary
                task_list.pop(id)

                # Write the remaining tasks to 'tasks.txt'
                with open("tasks.txt", "w") as f:
                    for each_key in task_list:
                        f.write(task_list[each_key].name + " - " + task_list[each_key].desc + "\n")
            elif id != 0:
                print("Não consegui encontrar a tua tarefa. Talvez me tenha esquecido dela...\n")   

        # Option to view all tasks
        elif option == 4:
            # Initialize an empty dictionary to store tasks
            task_list = {}
            # Read lines from 'tasks.txt' and create Task objects with task_id, name, and desc
            f = open("tasks.txt", "r").readlines()
            task_id = 1
            
            for line in f:
                if line.strip():
                    row = line.split('-')
                    name, desc = [i.strip() for i in row]
                    task_list[task_id] = Task(task_id, name, desc)
                    task_id += 1
                    
            # Display names and descriptions of all tasks
            for each_key in task_list:
                print(task_list[each_key].name + " ::: " + task_list[each_key].desc)

        # Option to exit the program
        elif option == 0:
            print("Até à próxima!")
            exit(1)
        
        else:
            print("Essa não é uma opção válida! Tenta de novo\n")
