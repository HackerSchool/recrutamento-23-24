from pysondb import db
# Visto que não consegui acabar a tempo, não cheguei a implementar a database do pysondb.
import sys, subprocess


def clear_screen():
    """
    Função que limpa o terminal, para que se torne mais facil a visualização do que esta a acontecer
    :return:
    """
    sistema_operativo = sys.platform
    if sistema_operativo == 'win32':
        subprocess.run('cls', shell=True)
    elif sistema_operativo == 'linux' or sistema_operativo == 'darwin':
        subprocess.run('clear', shell=True)


def criar_tasklist():
    """
    Função cria um dicionario vazio, para que possa ser prenchido com os eventos
    :return:
    """
    tasklist = {}
    return tasklist


def ask_input(prompt):
    """
    A função recebe uma string, e converte a string para letras pequenas, para que possa ser mais facil
    definir os acontecimentos
    :param prompt:
    :return:
    """
    return input(prompt).lower()


def descricao_evento(nome, tasklist):
    """
    A função recebe o nome do evento, e o dicionario da tasklist. E altera/cria a descrição do evento.
    :param nome:
    :param tasklist:
    :return:
    """
    descricao = input('Qual a descricao que deseja?')
    tasklist[nome]['descricao'] = descricao


def data_evento(nome, tasklist):
    """
    A função recebe o nome do evento, e o dicionario da tasklist. E altera/cria a data do evento.

    :param nome:
    :param tasklist:
    :return:
    """
    data = input('Qual a data que deseja')
    tasklist[nome]['data'] = data


def adicionar_evento(Tasklist):
    """
    Uma das funções principais, recebe um dicionario da tasklist e permite adicionar tarefas a um dicionario vazio
    :param Tasklist:
    :return:
    """
    while True:  # entra em loop para que caso as input estejam incorretas volte a pedir
        nome = ask_input('Digite o nome do evento que deseja criar')
        if nome in Tasklist:
            repetido = ask_input('já existe um evento com esse nome, gostaria de editar ou cancelar')
            if repetido == 'editar':
                editar_evento_existente(Tasklist, nome)
            elif repetido == 'cancelar':
                return
        elif nome not in Tasklist:
            Tasklist[nome] = {}
            data_evento(nome, Tasklist)
            descricao_evento(nome, Tasklist)
            clear_screen()
            print("Evento adicionado com sucesso")
            return Tasklist


def editar_evento_existente(tasklist, nome):
    """
    A função recebe o dicionario da tasklist e o nome do evento. Criada para simplificar quando o utilizador tenta
    adicionar um evento ja existente na agenda
    :param tasklist:
    :param nome:
    :return:
    """
    data_evento(nome, tasklist)
    descricao_evento(nome, tasklist)
    return tasklist


def dict_keys(dicionario):
    """
    Recebe o dicionario da Tasklist e devolve uma lista das chaves do dicionario
    :param dicionario:
    :return:
    """
    chaves = dicionario.keys()
    print(list(chaves))


def editar_evento(Tasklist):
    """
    A função recebe o dicionario da Tasklist. Vai pedir uma input ao utilizador que representa um nome do evento
    caso exista, vai voltar a pedir qual o parametro que deseja alterar
    :param Tasklist:
    :return:
    """
    clear_screen()
    while True:
        dict_keys(Tasklist)
        nome = ask_input('Qual o evento que gostaria de editar?')
        if nome not in Tasklist:
            print('input invalido')
            while True:
                input = ask_input('Gostaria de continuar ou sair?')
                if input == 'sair':
                    return
                if input == 'continuar':
                    break
                else:
                    print('input incorreto')
        else:
            while True:
                print('data,nome,descricao')
                parametro_a_mudar = ask_input('Pretende mudar algum parametro? Digite sair se pretender sair')
                if parametro_a_mudar in ('descricao', 'data'):
                    Tasklist[nome][parametro_a_mudar] = ask_input('Digite o novo parametro')
                elif parametro_a_mudar == 'nome':
                    Tasklist[nome] = ask_input('Digite o novo nome')
                elif parametro_a_mudar not in ('descricao', 'data', 'nome'):
                    print('Parametro incorreto')
                continuar = ask_input('Deseja continuar? "nao" para sair')
                if continuar in ('nao', 'não', 'no'):
                    return Tasklist


def remover_evento(Tasklist):
    """
    A função recebe o dicionario composto pelos eventos, da print das keys para facilitar a visualização. E pede por uma
    input, o nome do evento ou então sair para acabar o ciclo
    :param Tasklist:
    :return:
    """
    clear_screen()
    while True:
        dict_keys(Tasklist)
        inpututilizador = input('Caso Pretenda eliminar um evento digite o seu nome, ou sair')
        if inpututilizador in Tasklist:
            del Tasklist[inpututilizador]
            return Tasklist
        if inpututilizador == 'sair':
            return
        else:
            print('Input incorreto')


def mensagem_incial():
    """
    Mensagem inicial utilizada no inicio da funcao main
    :return:
    """
    print(
        'Olá bem vindo ao seu gerenciador de tarefas \nO que gostaria de fazer hoje?'
        '\n1.Visualizar a minha agenda'
        '\n2.Adicionar eventos'
        '\n3.Remover eventos'
        '\n4.Editar eventos'
        '\n5.Sair'
        '\n6.Help'
    )


def help():
    """
    Função para a documentação
    :return:
    """
    print('Projeto desenvolvido para o Recrutamente da Hackerschool'
          '\nI wish i add more time but algebra linear said no')


def visualizar_tarefas(database):  # Tentativa de implementar uma base de dados
    print(database.get())


def main():
    """
    função principal
    :return:
    """
    alteracoes = criar_tasklist()  # o nome era alterações, porque o intuito original era fazer com que a cada alteração fosse atualizada para a data base

    # 1database.add(dicionario)

    while True:  # entra em loop que apenas vai ser quebrado, caso o utilizador queira sair
        mensagem_incial()
        opcao = input('Digite o numero da opcão')
        if opcao == '6':
            help()
            input('... continuar')
        elif opcao == '5':
            break
        elif opcao == '4':
            editar_evento(alteracoes)
        elif opcao == '3':
            remover_evento(alteracoes)
        elif opcao == '2':
            adicionar_evento(alteracoes)
        elif opcao == '1':
            clear_screen()
            print(alteracoes)
            input('Pressione para continuar')
        else:
            clear_screen()
            print('A opcao introduzida nao existe, a voltar para o menu inicial')
            input('Pressione para continuar')


main()
