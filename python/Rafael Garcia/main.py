from core.Taskmsys import Taskmsys
from core.Tasks.TaskEnconder import TaskEncoder
from core.Tasks.TaskDecoder import TaskDecoder
from app.Menus.OpenMenu import OpenMenu
from libIO.MenuOpener import MenuOpener
import json

''' Gets the data from preivous session store in a the JSON file,'''
def load_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f, cls=TaskDecoder)
    except Exception:
        data = {}
        save_data(data)
    return data

''' Saves the data build up in this session in a JSON file'''
def save_data(data):
    with open("data.json", "w") as f:
        # Use the custom TaskEncoder to serialize Task objects
        json.dump(data, f, indent=2, cls=TaskEncoder)

''' Core of the app coordenates the userIO with the core of the app and the externals libraries
defining menu's and commands'''
def main():
    data = load_data()
    tsys = Taskmsys("", data)
    open_menu = OpenMenu("Open Menu", tsys)
    menu_opener = MenuOpener()
    menu_opener.open_menu(open_menu)
    save_data(tsys.tasks)
    return 0
    
if __name__=="__main__":
    main()