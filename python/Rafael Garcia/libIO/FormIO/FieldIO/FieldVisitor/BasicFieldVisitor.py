from libIO.FormIO.FieldIO.BasicIO.BasicIO import BasicIO
from lib.Commands.Forms.Fields.BooleanField import BooleanField
from lib.Commands.Forms.Fields.StringField import StringField
from lib.Commands.Forms.Fields.TimeField import TimeField
from libIO.FormIO.FieldIO.BasicIO.CustomErrors import *

''' Class responsible for getting user intput and storing it in the correct
data type field'''
class BasicFieldVisitor:
    def __init__(self) -> None:
        self._userIO = BasicIO()
    
    def parseBooleanField(self, field: BooleanField):
        while True:
            try:
                input = self._userIO.request_string(field.get_prompt())
                if field.parse(input):
                    break
                self._userIO.pop("Confirmation Must be 'yes', 'no', 'y' or 'n'")
            except EmptyString as es:
                self._userIO.pop(es)
        return True
                
    def parseStringField(self, field: StringField):
        while True:
            try:
                input = self._userIO.request_string(field.get_prompt())
                if field.parse(input):
                    break
            except EmptyString as es:
                self._userIO.pop(es)
        return True
                
    def parseTimeField(self, field: TimeField):
        while True:
            try:
                input = self._userIO.request_string(field.get_prompt())
                if field.parse(input):
                    break
                self._userIO.pop("Input Must Be in the format: DD/MM/YY")
            except EmptyString as es:
                self._userIO.pop(es)
        return True