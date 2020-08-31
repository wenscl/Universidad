from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from construct import Int8ub
from TpsParse.Utils.FieldType import FieldType

class ByteField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.Byte.name


    def get_value(self, input_stream):
        return Int8ub.parse(input_stream.read(1))