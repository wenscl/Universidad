from TpsParse.Utils.FieldType import FieldType
from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from TpsParse.Utils import BitUtil
from datetime import datetime


class DateField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.Date.name

    def get_value(self, input_stream):
        date = BitUtil.stream_to_int32u(input_stream)

        if date == 0:
            return None

        years = int((date & 0xFFFF0000) >> 16)
        months = int((date & 0x0000FF00) >> 8)
        days = int(date & 0x000000FF)

        return datetime(years, months, days)