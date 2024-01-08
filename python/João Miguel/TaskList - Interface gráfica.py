# importamos o tkinker, incluido na instação habitual do python
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


janela = Tk() #inicio da estrutura do ciclo infinito da janela principal
janela.title("TaskList") #nome da janela

tarefas = [] 

#vamos criar um bloco de texto na janela, como texto "Tasklist".
#padx e pady dizem o tamanho da janela
#.pack() faz um posicionamento automático 
# iremos ver mais do mesmo, pelo que é bom retornar aqui se necessário
Label1 = Label(janela, text="\n TaskList", padx=75, pady=40).pack() 

def novatarefa():
    global tarefas #para o tkinker, as variáveis locais têm de ser generalizadas para podermos usá-las
    i = 0
    titulo = tituloe.get() # .get busca o que está na caixa de texto, no caso  "tituloe"
    desc = desc_e.get()
    if len(titulo) == 0: #verifica se o nosso input não é vazio
        messagebox.showerror("error!", "título inválido!")

    if len(desc) == 0:
        messagebox.showerror("error!", "descrição inválida!")

    while i < len(tarefas) and titulo != tarefas[i][0]:
        i +=1

    if i != len(tarefas):
        messagebox.showerror("error!","Já existe uma tarefa com o mesmo nome!, tente novamente.")
        
    
    else:   
        if len(desc) != 0 and len(titulo) != 0:
            tarefas += [[titulo, desc]]
            messagebox.showinfo("informação","tarefa criada com sucesso!")

def eliminartarefa(): # os alogoritmos são adaptados da versão CLI
        global tarefas
        titulo = tituloeliminar.get()
        i = 0
        if len(tarefas) != 0:
            while i < len(tarefas) and titulo != tarefas[i][0]:
                i +=1
            if i != len(tarefas):
                tarefas = tarefas[:i] + tarefas[i+1:]
                messagebox.showinfo("informação","tarefa removida com sucesso!")
            else:
                messagebox.showerror("error!","a tarefa \"{}\" não existe!".format(titulo))
        else:
            messagebox.showerror("error!","não há tarefas para eliminar!")

def editartarefa():
        titulo = janelaeditar_e.get()
        i = 0
        j = 0
        while i < len(tarefas) and titulo != tarefas[i][0]:
            i += 1
        if i == len(tarefas):
            messagebox.showerror("error!","a tarefa \"{}\" não existe!".format(titulo)) 

        else:
            ntitulo =  janelaeditar_n_titulo.get()
            ndesc = janelaeditar_n_editar.get()
            while j < len(tarefas) and ntitulo != tarefas[j][0]:
                j +=1
            if j != len(tarefas):
                messagebox.showerror("error!","Já existe uma tarefa com o mesmo nome!, tente novamente.")
                
            else:   
                if ntitulo == "":
                    ntitulo = titulo
                if ndesc == "":
                    ndesc = tarefas[i][1]   
                
                tarefas[i][0] = ntitulo
                tarefas[i][1] = ndesc
                messagebox.showinfo("informação","tarefa editada com sucesso!")  
                        
            
            

    

def listadetarefas():
    global tarefas,linha,tabela,item
    
    p = 0
    i = 0
    listadeinfo = []
    while i < len(tarefas):
        linha = (str(tarefas[i][0]), str(tarefas[i][1]))
        listadeinfo.append(linha)
        i += 1

    for item in tabela.get_children():
        tabela.delete(item)
    
    while p < len(listadeinfo):
        tabela.insert(parent='', index="end", iid=p, values = listadeinfo[p])
        p += 1
        
        
#criação de janelas extras
def openjanelaeditar(): 
    global janelaeditar, janelaeditar_n_titulo,janelaeditar_n_editar , submitButton, Label2editar, Label_n_titulo, Label_n_desc, janelaeditar_e
    janelaeditar = Toplevel(padx=50,pady=50) #tamanho da janela
    janelaeditar.title("editar uma tarefa")
    Label2editar = Label(janelaeditar, text="nome da tarefa:", padx=75, pady=40).pack()
    janelaeditar_e = Entry(janelaeditar) #estrutura de input de texto
    janelaeditar_e.pack() 
    Label_n_titulo = Label(janelaeditar, text="novo nome da tarefa:", padx=75, pady=40).pack()
    janelaeditar_n_titulo = Entry(janelaeditar) #same
    janelaeditar_n_titulo.pack()
    Label_n_desc = Label(janelaeditar, text="nova descrição da tarefa:", padx=75, pady=40).pack()
    janelaeditar_n_editar = Entry(janelaeditar) #here too
    janelaeditar_n_editar.pack()
    submitButton = Button(janelaeditar, text="submit", command=editartarefa).pack()

def openjanelaeliminar():
    global tituloeliminar, Label2eliminar,submitButton
    janelaeliminar = Toplevel(padx=50,pady=50)
    janelaeliminar.title("eliminar uma tarefa")
    tituloeliminar = Entry(janelaeliminar)
    tituloeliminar.pack()
    Label2eliminar = Label(janelaeliminar, text="nome da tarefa:", padx=75, pady=40).pack()
    submitButton = Button(janelaeliminar, text="submit", command=eliminartarefa).pack()
    
def openjanelacriar():
    global tituloe, submitButton, Label2,Labeldesc, desc_e
    janelacriar = Toplevel(padx=50,pady=50)
    janelacriar.title("criar uma tarefa")
    Label2 = Label(janelacriar, text="nome da tarefa:", padx=75, pady=40).pack()
    tituloe = Entry(janelacriar)
    tituloe.pack()
    Labeldesc = Label(janelacriar, text="descrição da tarefa:", padx=75, pady=40).pack()
    desc_e = Entry(janelacriar)
    desc_e.pack()
    submitButton = Button(janelacriar, text="submit", command=novatarefa).pack()

def openjanelalista():
    global tasks,refreshbutton,c,d,janelalista,tabela
    janelalista = Toplevel(padx=50,pady=50)
    janelalista.title("lista de tarefas")
    refreshbutton = Button(janelalista, text="refresh", command=listadetarefas).pack()
    tabela = ttk.Treeview(janelalista)
    tabela['columns'] = ("nome","descrição")
    tabela.column("#0", width=0)
    tabela.column("nome")
    tabela.column("descrição")
    tabela.heading("nome", text="nome")
    tabela.heading("descrição", text="descrição")   
    tabela.pack()
    

Button1 = Button(janela, text="criar", command=openjanelacriar).pack()
Button2 = Button(janela, text="eliminar", command=openjanelaeliminar).pack()
Button3 = Button(janela, text="editar",command=openjanelaeditar).pack()
Button4 = Button(janela, text="ver lista de tarefas",command=openjanelalista).pack()



janela.mainloop() #estrutura limitadora do ciclo infinito da janela principal