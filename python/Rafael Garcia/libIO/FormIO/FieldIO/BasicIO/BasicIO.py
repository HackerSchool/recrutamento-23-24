from libIO.FormIO.FieldIO.BasicIO.CustomErrors import *

''' Class repsonsible for every input / ouput off the all app
Core of the design of the tashlist'''
class BasicIO:
    def __init__(self):
        self.text = ""
        
    def request_string(self, p):
        lb = input(p)
        lb = lb.strip()
        if lb == "":
            raise EmptyString("No string was provided")
        return lb
    
    def request_number(self, p):
        lb = input(p)
        lb = lb.strip()
        if lb.isdigit():
            return int(lb)
        raise InvalidNumber("Wrong Input (ENTER positive number Ex: 1)")
    
    ''' Returns the buffer'''
    def texted(self):
        return self.text
    
    ''' Quickly displays a prompt given in stdout'''
    def pop(self, p):
        print(p)
    
    ''' Displat what has been stores in the local buffer'''
    def display(self):
        self.pop(self.text)
        self.clear()

    ''' Resets the local buffer'''
    def clear(self):
        self.text = ""

    ''' Adds text to the local buffer, Given b false, this functions doesnt add a new line 
    to the buffer, otherwise the add'''
    def addText(self, p, b):
        self.text += p
        if b:
            self.addLine()
      
    ''' Adds a to the to the buffer'''      
    def addLine(self):
        self.text += "\n"


