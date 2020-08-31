from TpsParse.Utils.FieldType import FieldType
from TpsParse.Fields.StringField import StringField

class FixedLengthStringField(StringField):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.type = FieldType.FixedLengthString.name


    def get_value(self, input_stream):
        buffer = input_stream.read(self.length)

        return buffer.decode("iso-8859-1")