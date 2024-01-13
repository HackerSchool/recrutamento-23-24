
#TaskList project para hackerschool, feito por Henrique Delfino
lista_titulo = [] #lista para os titulos das tarefas
lista_descricao = [] #lista para a descrição das tarefas
counter = 0 #countador de tarefas
while True:
    #Interface inicial
    print("Olá seu perguiçoso, o que pretendes fazer?")
    print("para adicionar tarefa prime 1")
    print("para apagar tarefa prime 2")
    print("para editar tarefa prime 3")
    print("para vizualizar tarefa prime 4")
    print("para sair prime 5")
    
    numero = input("Escolhe a opção entre 1 e 5: ") 
    #caso o utilizador pretenda adicionar uma tarefa, este if statement irá adicionar uma tarefa
    if numero == '1':
        print("adiciona tarefa")
        lista_titulo.append(counter)
        lista_titulo[counter] = input("Qual o titulo da tua tarefa?")
        lista_descricao.append(counter)
        lista_descricao[counter] = input("Qual a descrição da tua tarefa?")
        counter = counter + 1
    #caso o utlizador pretenda apagar uma tarefa, este if statment irá remover a tarefa escolhida pelo utilizador
    elif numero == '2':
        i = 0
        encontrou = False
        tarefapagada = input("Qual o título da tarefa que pretendes apagar?")
        while i < counter:
            if tarefapagada == lista_titulo[i]:
                print(i)
                print("      " + lista_titulo[i] + "      ")
                print(lista_descricao[i])
                lista_titulo.pop(i)
                lista_descricao.pop(i)
                counter = counter - 1
                encontrou = True
                break
            i = i + 1
        if encontrou == False:
         print("tarefa não encontrada") 
    #caso o utilizador pretenda editar a tarefa, este if statment irá pedir ao utilizador o titulo da tarefa a editar e consequentemente editá-la
    elif numero == '3':
        i = 0
        encontrou = False
        tarefaeditada = input("escreve o titulo da tarefa que pretendes editar")
        while i < counter:
            if tarefaeditada == lista_titulo[i]:
                print(i)
                print("      " + lista_titulo[i] + "      ")
                print(lista_descricao[i])
                lista_titulo[i] = input("qual o novo titulo?")
                lista_descricao[i] = input("qual a nova descrição?")
                encontrou = True
                break
            i = i + 1
        if encontrou == False:
         print("tarefa não encontrada") 
    #caso o utliziador pretenda visualizar a lista de tarefas 
    elif numero == '4':
        print("visualizando")
        i = 0
        while i < counter:
            print(i + 1)
            print("      " + lista_titulo[i] + "      ")
            print(lista_descricao[i])
            i = i + 1
    #caso o utilizador pretenda sair do programa
    elif numero == '5':
        print("a sair, obrigado")
        break
    #caso o input não corresponda a nenhuma aplicação disponivel
    else : 
        print("Input incorreto, isso nao foi nem 1 nem 2 nem 3 nem 4 nem 5")



