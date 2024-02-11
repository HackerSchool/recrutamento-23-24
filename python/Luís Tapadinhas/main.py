import tkinter as tk

#adicionar uma task
def adicionar_task():
 tarefa_nome = task_get.get()
 
 if tarefa_nome:
  lista_tasks.insert(tk.END,tarefa_nome)
  task_get.delete(0,tk.END)
  data_base = open("database.txt","a")
  import time
  tempo = time.strftime('%I:%M:%S %p %Z')
  taskss = lista_tasks.get(0,tk.END)
  dats = lista_datas.get(0,tk.END)
  for i, k in zip(taskss,dats):
     data_base.write( tempo +   f"{i} - {k}\n") 
 #adicionar data à task 
 def adicionar_data():
  data_nome = task_get_j1.get()
  
  if data_nome:
   lista_datas.insert(tk.END,data_nome)
   task_get_j1.delete(0,tk.END)
   janela1.destroy()

  data_base = open("database.txt","a")
  import time
  tempo = time.strftime('%I:%M:%S %p %Z')
  taskss = lista_tasks.get(0,tk.END)
  dats = lista_datas.get(0,tk.END)
  for i, k in zip(taskss,dats):
     data_base.write( tempo +   f"{i} - {k}\n") 
  else:
   titulo_j1 = tk.Label(janela1,text = "Coloque 'não' ou selecione uma data") 
   titulo_j1.place(x=5,y=1)

 janela1 = tk.Tk()
 janela1.geometry("200x80")
 janela1.resizable(False,False)
 
 titulo_j1 = tk.Label(janela1,text = "Pretende colocar data??") 
 titulo_j1.place(x=30,y=1)

 task_get_j1 = tk.Entry(janela1,width=25)
 task_get_j1.place(x=25,y=25)

 botão_j1 = tk.Button(janela1,text = "Sim", command=adicionar_data )
 botão_j1.place(x=30,y=50)
 
 botão_j1_1 = tk.Button(janela1,text = "Não", command=janela1.destroy)
 botão_j1_1.place(x=130,y=50)
 
 #salvar dados em ficheiro
def save_tasks_datas():
 f=open('savefile.txt','w') 

 taskss = lista_tasks.get(0,tk.END)
 dats = lista_datas.get(0,tk.END)
 for i, k in zip(taskss,dats):
  f.write(f"{i} - {k}\n")  
   
#retirar task
def retirar_task():
 janela2 = tk.Tk()
 janela2.geometry("200x80")
 janela2.resizable(False,False)
 
 titulo_j2 = tk.Label(janela2,text = "Tem a certeza? Se sim escolha uma opção") 
 titulo_j2.place(x=30,y=1)

 def apagar_task_processo():
   tarefa_nome1 = lista_tasks.curselection()
   lista_tasks.delete(tarefa_nome1)
   janela2.destroy()

 def apagar_data_processo():
   data_nome1 = lista_datas.curselection()
   lista_datas.delete(data_nome1)
   janela2.destroy()


 botão_j2_1 = tk.Button(janela2,text ="Task", command= apagar_task_processo)
 botão_j2_1.place(x=30,y=50)

 botão_j2_2 = tk.Button(janela2,text="Data", command = apagar_data_processo)
 botão_j2_2.place(x=130,y=50)

  
 
def ajuda():
 janela3 = tk.Tk()
 janela3.geometry("160x120")
 janela3.resizable(False,False)
 infor_text= "Este programa consiste num gestor de tarefas, para qualquer tipo de tarefas, sendo possível também atribuir uma data para facilitar a organização"
 infor = tk.Message(janela3,text=infor_text)
 infor.place(x=0,y=0)

def clear():
 lista_datas.delete(0,tk.END)
 lista_tasks.delete(0,tk.END)

#interface gráfica
janela = tk.Tk()
janela.title("janela")
janela.geometry("600x600")
janela.resizable(False,False)

titulo = tk.Label(janela,text = "Task manager app") #mudar a letra e o tamanho
titulo.place(x=250,y=0)

botão = tk.Button(janela,text="adicionar",width=15, command=adicionar_task)
botão.place(x=50,y=75)

botão1 = tk.Button(janela,text="save",width=15,command=save_tasks_datas)
botão1.place(x=250,y=75)

botão2 = tk.Button(janela,text="retirar",width=15, command=retirar_task)
botão2.place(x=450,y=75)

lista_tasks = tk.Listbox(janela, width=300,height=25)
lista_tasks.place(x=0,y=150)

lista_datas = tk.Listbox(janela,width=300,height=25)
lista_datas.place(x=300,y=150)

task_get = tk.Entry(janela,width=50)
task_get.place(x=150,y=25)

botão3 = tk.Button(janela,text="?",width=1,height=0,command=ajuda)
botão3.place(x=578,y=568)

botão4 = tk.Button(janela,text="clc",width=1,height=0,command=clear)
botão4.place(x=578,y=528)

janela.mainloop()