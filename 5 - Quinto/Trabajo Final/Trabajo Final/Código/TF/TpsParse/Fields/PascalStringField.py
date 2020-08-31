from TpsParse.Utils.FieldType import FieldType
from TpsParse.Fields.StringField import StringField

class PascalStringField(StringField):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.PascalString.name


    def get_value(self, input_stream):
        len = input_stream.read(1)
        buffer = input_stream.read(len)

        return buffer.decode("iso-8859-1")