from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from construct import Float64b

class DoubleField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.Double.name


    def get_value(self, input_stream):
        buffer = input_stream.read(8)

        return Float64b.parse(buffer)