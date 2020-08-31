from TpsParse.Utils.FieldType import FieldType
from TpsParse.Fields.StringField import StringField
from TpsParse.Utils import BitUtil

class ZeroTerminatedStringField(StringField):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.ZeroTerminatedString.name


    def get_value(self, input_stream):
    
        return BitUtil.zero_terminated_string(input_stream)