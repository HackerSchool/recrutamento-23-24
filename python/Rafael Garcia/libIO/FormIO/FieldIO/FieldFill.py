from lib.Commands.Forms.Fields.Field import Field
from libIO.FormIO.FieldIO.FieldVisitor.BasicFieldVisitor import BasicFieldVisitor

''' Classing representing a field filler which, as the name sugest
gets user input and stores in the correct data type'''
class FieldFill:
    def __init__(self) -> None:
        self.field_visitor = BasicFieldVisitor()
    
    def fill_field(self, field: Field):
        return field.accept(self.field_visitor)
