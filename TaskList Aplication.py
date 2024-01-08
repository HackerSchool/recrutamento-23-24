from _tkinter import *

# cp = lista de comandos possíveis
cp = ["help", "1", "2", "3", "4"] 

#lista de tarefas (lista de listas)
tarefas = [] 

#as tarefas são listas, onde a primeira entrada é o título e a segunda, a descrição
print("\n TaskList - Como usar? \n escreva o comando exit para sair.  \n\n Digite:\n \n 1- adicionar tarefa \n 2- remover tarefa \n 3- editar tarefa \n 4- ver todas as tarefas \n \n Dica: podes sempre voltar a ver este menu digitando help.")
resposta = input("\n Digite um comando: ")



#ciclo infinito para o input do usuário
while resposta != "exit": 

    if resposta not in cp: 
        print("Erro! não foi dado um comando válido.")

    if resposta == "help":
        print("TaskList - Como usar? \n Dica: podes sempre voltar a ver este menu digitando Help. \n Digite:\n \n 1- adicionar tarefa \n 2- remover tarefa \n 3- editar tarefa \n 4- ver todas as tarefas \n 5 -")
        


    if resposta == "1":
        i = 0
        titulo = input("\n título da nova tarefa: ")
        
        while titulo == "":
            print("\n título inválido, tente novamente")
            titulo = input("\n título da nova tarefa: ")

        while i < len(tarefas) and titulo != tarefas[i][0]: # percorremos toda a lista em busca de uma tarefa com o mesmo nome
            i +=1
        if i != len(tarefas): # se não tivermos percorrido toda a lista, é porque encontramos alguma com o mesmo nome
            print("Já existe uma tarefa com o mesmo nome!, tente novamente.")

        
        if i == len(tarefas): # se percorremos toda, não encontramos
            desc = input("\n descrição: ")    
            tarefas += [[titulo, desc]]
            print("tarefa criada com sucesso!")

       
# Nenhum ser humano tem tantas tarefas tal que precise de um algoritmo de persquisa binária, portanto podemos ver elemento a elemento sem grande perda de eficiência.

    if resposta == "2":         
        titulo = input("\n título da tarefa: ")
        i = 0
        if len(tarefas) != 0: # não podemos eliminar tarefas se não existirem tarefas
            while i < len(tarefas) and titulo != tarefas[i][0]: # mesma ideia do while anterior
                i +=1
            
            if i != len(tarefas):
                tarefas = tarefas[:i] + tarefas[i+1:] #fazemos um slice da lista e retiramos o elemento
                
                print("tarefa removida com sucesso!")
            else: 
                print("a tarefa \"{}\" não existe!".format(titulo))



    if resposta == "3":
        titulo = input("\n título da tarefa: ")
        i = 0
        while i < len(tarefas) and titulo != tarefas[i][0]: #same  
            i += 1
        if i == len(tarefas):
            print("a tarefa \"{}\" não existe!".format(titulo)) 

        else:
            ntitulo = input("novo título da tarefa: ")
            ndesc = input("nova descrição: ")
        
            if ntitulo == "": # se o usuário quer ser estúpido, não o deixaremos 
                ntitulo = titulo
            if ndesc == "":
                ndesc == tarefas[i][1]   
            
            tarefas[i][0] = ntitulo
            tarefas[i][1] = ndesc
            print("tarefa editada com sucesso!")  
        


    if resposta == "4":
        if len(tarefas) == 0:
            print("Lista de tarefas vazia!")
        else:
            i = 0
            while i < len(tarefas): # organizamos as tarefas por números (facilita a leitura)
                    print("\n tarefa {}:\n \n título:".format(i), tarefas[i][0])
                    print(" descrição:", tarefas[i][1])
                    i += 1 

        
    
    resposta = input("\n Digite um comando: ") 
    
    
