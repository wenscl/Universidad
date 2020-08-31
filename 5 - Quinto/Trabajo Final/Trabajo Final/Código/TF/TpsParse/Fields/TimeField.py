from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from TpsParse.Utils import BitUtil
from datetime import time as T


class TimeField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.Time.name

    def get_value(self, input_stream):
        time = BitUtil.stream_to_int32(input_stream)
        mins = (time & 0x00FF0000) >> 16
        hours = (time & 0x7F000000) >> 24

        return T(hours, mins)