#Alexandre Carapeto Delgado
#Hackerschool 2023/2024
#Projeto Python para recrutamento


'''
Raciocínio base


      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
     /                                            \ 
    v                                              \ 
start() ---> main() ---> command function ---> main()
                \ 
                 \ ---> time_to_exit()


ficheiro tasklist.txt que foi criado no $HOME directory é lido e guardado no dicionário tasks

start() function é chamada
start() pede input e chama main()
main() recebe e interpreta o input
main() chama uma das funções para os comandos
comando é executado e volta para a main()
main() chama start() de novo

programa só para quando o input dado for exit
aí, main() chama time_to_exit()
dicionário tasks é guardado no ficheiro
programa acaba
'''





#==== READ TASKLIST FROM FILE ====
import os

home_dir = os.path.expanduser("~")
tasks_file = open(str(home_dir) + "/tasklist.txt", "r")

tasks = {}

for i in tasks_file.readlines():
    #separar o texto antes dos primeiros : que têm um espaço a seguir do restante texto. Será o título da task e a descrição
    split_line = i.split(": ")
    
    #no caso de existirem na descrição mais : com espaços a seguir, simplesmente juntamos todo o texto
    task_desc = ": ".join(split_line[1:])

    #se não houver descrição, retira-se o \n do título da task, se houver descrição retira-se da descrição
    #\n conta como apenas um character
    if task_desc == "":
        tasks[split_line[0][:-1]] = task_desc
    else:
        tasks[split_line[0]] = task_desc[:-1]


tasks_file.close()



#==== ERROR MESSAGES ====
def command_error(order):
    print("Command not found: " + order)
    

def syntax_error(order):
    print("Invalid syntax: " + order + " is not a valid parameter.\ndo \"taskpy help\" for help")


def no_task_specified():
    print("No task specified.") 


def task_not_found():
    print("Task not found.")



#==== COMMANDS ====
def help_message():
    print("\nadd <title of task> <description> - Adds a task\nremove <title or number of task> - Removes a task\nlist - Displays the tasklist\nget <title or number of task> - Displays a task\nedit <title or number of task> <new description> - Edits a task\nexit - Exits and writes changes\nhelp - Displays this message\n")



def add(title, desc):
    #se apenas for feito o comando add sem argumentos dá erro e função para e volta para a main() (onde ocorre o restart do programa)
    if title == "":
        no_task_specified()
        
    #se correr tudo bem adicionamos a task ao dicionário
    else:
        tasks[title] = desc



#title pode ser o título da task ou o seu índice
def remove(title):
    #se não for introduzido nada, dá erro
    if title == "":
        no_task_specified()

    #se for introduzido o nome da task, removemo-la do dicionário tasks
    elif title in tasks: 
        if tasks[title] == "":
            print("Removed " + title)

        #se tiver descricao inclui-se na mensagem
        else:
            print("Removed " + title + ": " + tasks[title])  

        del(tasks[title])

    #se for introduzido o número da task
    else:
        try:
            keys = list(tasks)
            #converte o número para o título
            actual_title = keys[int(title)-1]
            #remove a task, agora passando mesmo o título da task
            remove(actual_title)
        
        #no caso da string não estar no dicionário ou do número não ser um dos índices
        except (ValueError, IndexError):
            task_not_found()
    
    #tanto no caso desta função, como na get() e na edit() é prioritizado o nome em vez do índice
    #assim, por exemplo, se uma task tiver como título o número 2 se nos referenciarmos a uma task como 2, estamos a apontar para a task com o título 2, não para a que tem índice 2


 

def list_tasks():
    keys = list(tasks)

    print("To-do:")
    for i in range(len(keys)):
    
        #se não houver descrição, mostramos o índice e o título da task
        if tasks.get(keys[i]) == "":
            print("(" + str(i+1) + ") " + str(keys[i]))

        #se houver descrição, o formato é (1) task: description, onde 1 é qualquer índice
        else:
            print("(" + str(i+1) + ") " + str(keys[i]) + ": " + str(tasks[keys[i]]))


            
def get(title):
    #se não for introduzido nenhuma task dá erro
    if title == "":
        no_task_specified()

    #se for introduzido o nome da task
    elif title in tasks:
        if tasks[title] == "":
            print(title)
        else:
            print(title + ": " + tasks[title])

    #se for introduzido o numero da task
    else:
        try:
            keys = list(tasks)
            #converte-se para o título mesmo, tal como no remove(), e chama-se a função de novo
            actual_title = keys[int(title)-1]
            
            get(actual_title)

        #no caso da string não 
        except (ValueError, IndexError):
            task_not_found()

 

#title pode ser o título da task ou o seu índice
def edit(title, newdesc):
    #se não for introduzido nada
    if title == "":
        no_task_specified()

    #se for introduzido o nome da task
    elif title in tasks:
        print("Edited " + title)
        tasks[title] = newdesc


    #se for introduzido o numero da task
    else:
        try:
            keys = list(tasks)
            actual_title = keys[int(title)-1]
            edit(actual_title, newdesc)

        #no caso da string não estar no dicionário ou do número não ser um dos índices
        except (ValueError, IndexError):
            task_not_found()

          
  
 

#=== BASE FUNCTIONS ===

#é sempre chamada após um comando para pedir input continuamente, com exceção do comando para sair
def start():
    #para dar reset ao comando (lista command) sempre que a funcao é chamada
    command = []

    call = input("> ")
    command = call.split()
    
    #preencher os parâmetros não introduzidos com filler
    while len(command) < 3:
        command.append("")
    
    #juntar todos os argumentos a partir do terceiro (índices começam em 0) para formar a descrição
    desc = " ".join(command[2:])
    
    #chama-se main() passando os vários parâmetros do comando
    main(command[0], command[1], desc)


#guarda o dicionário tasks no ficheiro
def time_to_exit():
    tasks_file = open(str(home_dir) + "/tasklist.txt", "w")
    
    for i in tasks:
        #se náo houver descrição para a task apenas escrevemos a task
        if tasks[i] == "":
            tasks_file.writelines(i + "\n")

        #se houver descrição escrevemos no mesmo formato usado no list_tasks()
        else:
            tasks_file.writelines(i + ": " + tasks[i] + "\n")
    
    tasks_file.close()


#função principal que interpreta os parâmetros do comando
def main(order, param1, param2):
    #se o user quiser parar o programa não se volta a chamar start()
    if order == "exit":
        time_to_exit()

    #se não, chamamos a função do comando correto e chamamos o start() para manter o programa a funcionar
    else:
        #se não for passado um comando válido dá erro
        if order not in ["help", "add", "remove", "list", "get", "edit"]:
            command_error(order)
        
        elif order == "help":
            help_message()

        elif order == "add":
            add(param1, param2) 

        elif order == "remove":
            remove(param1)
    
        elif order == "list":
            list_tasks()

        elif order == "get":
            get(param1)

        elif order == "edit":
            edit(param1, param2)


        start()


    return




#Começa o programa
start()
