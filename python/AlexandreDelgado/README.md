# Projeto Python Recrutamento Hackerschool 2023-2024

## Alexandre Carapeto Delgado


## Esta pasta contém:

este ficheiro `README.md`, o shell script `setup.sh`, o ficheiro `tasklist.py` e o ficheiro `preinstall_tasklist.py`

O `tasklist.py` será alterado depois do `setup.sh` ser corrido (mas é apenas uma linha que é adicionada)

O `preinstall_tasklist.py` existe como backup e guardar o script original



## Como correr/instalar o script



### Fazer apenas python3 tasklist.py

(é preciso criar ficheiro `tasklist.txt` no directory /home/username/)



----ou----


### Adicionar como shell command:


1. Adicionar shebang line na primeira linha do ficheiro com o environment correto

`#!/usr/bin/python3`


 ^este funcionou para mim, mas poderá ter que ser

`#!/usr/bin/python` ou `#!/usr/bin/env python`


2. Tornar script executável com

```
chmod +x tasklist.py
```


3. Adicionar ao PATH 
```
export PATH=$PATH:<path to script>
```
ou a `/usr/local/bin`




4. Criar ficheiro `tasklist.txt` no home/username directory (~)



Correr o script setup.sh como sudo para fazer estes passos 
```
sudo bash setup.sh
```

Este script modifica o ficheiro "tasklist.py", mas há sempre o ficheiro preinstall que permanece inalterado


----ou----


### Adicionar como alias

```
alias taskpy='python <path to script>.py'
```
