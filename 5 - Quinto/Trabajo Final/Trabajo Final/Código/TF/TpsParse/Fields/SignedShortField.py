from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from TpsParse.Utils import BitUtil

class SignedShortField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.SignedShort.name


    def get_value(self, inputStream):

        return BitUtil.stream_to_int16(inputStream)
