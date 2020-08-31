from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord

class GroupField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.Group.name


    def get_value(self, input_stream):
        buffer = input_stream.read(self.length)
        
        return buffer