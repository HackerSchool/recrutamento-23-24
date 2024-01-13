from lib.Commands.Forms.Form import Form
from lib.Commands.Forms.Fields.Field import Field
from libIO.FormIO.FieldIO.FieldFill import FieldFill

''' Class representing for filling a form for a particular command'''
class FormFill:
    def __init__(self) -> None:
        self.field_filler = FieldFill()
    
    def fill_form(self, form: Form):
        fields = form.get_fields()
        for title in fields:
            if not self.field_filler.fill_field(fields[title]):
                return False
        return True