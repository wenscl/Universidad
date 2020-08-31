from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from TpsParse.Utils import BitUtil


class SignedLongField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.SignedLong.name

    def get_value(self, input_stream):

        return BitUtil.stream_to_int32(input_stream)