from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from TpsParse.Utils import BitUtil

class UnsignedShortField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.UnsignedShort.name


    def get_value(self, input_stream):
        
        return BitUtil.stream_to_int16u(input_stream)