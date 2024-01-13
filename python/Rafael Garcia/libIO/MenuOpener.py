from lib.Menu import Menu
from lib.Commands.Command import Command
from libIO.FormIO.FieldIO.BasicIO.BasicIO import BasicIO
from libIO.FormIO.FieldIO.BasicIO.CustomErrors import InvalidNumber

''' Class responsible for opening any menu and display the user's commands '''
class MenuOpener:
    def __init__(self) -> None:
        self.userIO = BasicIO()
        
    def open_menu(self, menu: Menu):
        while True:
            self.userIO.addLine()
            self.userIO.addText("0 - Exit", True)
            for entry in range(0, menu.size()):
                command: Command = menu.get_command(entry)
                self.userIO.addText(f"{entry + 1} - {command.get_prompt()}", True)
            self.userIO.display()
            
            ''' Gets user command '''
            try:
                commmand_entry = self.userIO.request_number("Please Insert a Command: ")
                if commmand_entry < 0 or commmand_entry > menu.size():
                    self.userIO.pop("Please ENTER the number of a command displayed on the menu")
                    continue
                if commmand_entry == 0:
                    break
                command: Command =  menu.get_command(commmand_entry - 1)
                if not command.execute():
                    self.userIO.pop("Leaving Command . . .")
            except InvalidNumber as inv:
                self.userIO.pop(inv)
                
        return True
                
                
        