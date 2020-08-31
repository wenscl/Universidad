import re

from TpsParse.Record.FieldDefinitionRecord import FieldDefinitionRecord
from decimal import Decimal
from construct import Int8ub
from TpsParse.Utils.FieldType import FieldType

class BcdField(FieldDefinitionRecord):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.bcd_digits_after_decimal_point = input_stream.read(1)
        self.bcd_length_of_element = input_stream.read(1)
        self.type = FieldType.Bcd.name


    def get_value(self, input_stream):
        buffer = input_stream.read(Int8ub.parse(self.bcd_length_of_element))
        string = ''.join([format(b,'02x') for b in buffer])
        sign = string[0]
        number = string[1:]
        if self.bcd_digits_after_decimal_point > bytes([0]):
            decimal_index = len(number) - Int8ub.parse(self.bcd_digits_after_decimal_point)
            number = number[0:decimal_index] + '.' + number[decimal_index:]

        _ = "-" if sign != "0" else ""
        number = re.sub(r"[a-zA-Z]+", "", number)
        return Decimal(_ + number.lstrip('0'))
