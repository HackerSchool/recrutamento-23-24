

#por PEDRO NANTES e HUGO FONA







from msilib.schema import CreateFolder
task_list = []
class CREATE_TASK:
    task_code = 1
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.code = CREATE_TASK.task_code
        CREATE_TASK.task_code += 1

def ADD_TASK(parts):
    
    global task_list
    
    if len(parts) >= 3:
        
        title = parts[1]
        
        description = " ".join(parts[2:])
        
        new_task = CREATE_TASK(title, description)
        
        task_list.append(new_task)
        
        print(f"Task '{title}' added successfully.")
        
    else:
        
        print("Invalid command format. Use 'ADD_TASK Title Description'.") 
                
def REMOVE_TASK(parts):
    global task_list
    
    if(len(parts)== 2):
        
        try:
            code = int(parts[1])
            
            for task in task_list:
                
                if (task.code == code):
                    
                    task_list.remove(task)
                    
                    print(f"Task with code {code} removed successfully.")
                    return
            
            print(f"Task with code {code} not found.")
        except ValueError:
            
            print("Invalid command format. Use 'REMOVE_TASK Code'.")
    else:
        print("Invalid command format. Use 'REMOVE_TASK Code'.")

def SHOW_LIST():
    
    global task_list
    
    for task in task_list:
        
            print(f"Title: {task.title}, Code: {task.code}")

def EDIT_TASK(parts):
    global task_list
    
    if len(parts) == 3:
        
        for task in task_list:
            try:
                
                if(int(parts[2]) == task.code):
                
                    if(parts[1] == "TITLE"):
                    
                        task.title = input("Enter a new title ")
                        return;
                
                    elif(parts[1] == "DESCRIPTION"):
                    
                        task.description = input("Enter a new description ")
                        return;
            except ValueError:
                print("Invalid code")   

        print("Invalid code")           
    else:
        
        print("Invalid command")
    
Query = {
    "ADD_TASK": ADD_TASK,
    "REMOVE_TASK": REMOVE_TASK,
    "EDIT_TASK": EDIT_TASK,
    "SHOW_LIST": SHOW_LIST
}
  
while True:    
    uinput = input("Enter ADD_TASK Title Description/REMOVE_TASK Code/EDIT_TASK TITLE/DESCRIPTION CODE/SHOW_LIST/QUIT: ")
    parts = uinput.split(" ")
    
    if uinput in Query:
        
        Query[uinput]()
        
    elif parts[0] in Query:
        
        Query[parts[0]](parts)
        
    elif uinput == "QUIT":
        
        print("Stopping...")
        break;
    
    else:
        print("Invalid command")