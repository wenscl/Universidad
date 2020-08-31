from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from construct import Float32b

class FloatField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.Float.name


    def get_value(self, input_stream):
        buffer = input_stream.read(4)

        return Float32b.parse(buffer)