from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from TpsParse.Utils import BitUtil
from abc import ABC

class StringField(FieldDefinitionRecord, ABC):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.string_length = BitUtil.stream_to_int16(input_stream)
        self.string_mask = BitUtil.zero_terminated_string(input_stream)
        if len(self.string_mask) == 0:
            input_stream.read(1)