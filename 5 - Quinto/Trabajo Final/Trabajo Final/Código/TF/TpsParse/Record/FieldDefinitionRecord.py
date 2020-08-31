from abc import ABC, abstractmethod
from TpsParse.Utils import BitUtil

class FieldDefinitionRecord(ABC):
    def __init__(self, input_stream):
        self.offset = BitUtil.stream_to_int16(input_stream)
        self.field_name = BitUtil.zero_terminated_string(input_stream)
        self.elements = BitUtil.stream_to_int16(input_stream)
        self.length = BitUtil.stream_to_int16(input_stream)
        self.flags = BitUtil.stream_to_int16(input_stream)
        self.index = BitUtil.stream_to_int16(input_stream)

    @abstractmethod
    def get_value(self, input_stream):
        pass

    # Specifies whether or not this field contains an array.
    # returns true if the field is an array.
    def is_array(self):

        return self.elements > 1
    
    # Gets the array value if applicable.
    # returns an array of values.
    def get_array_value(self, input_stream):
        values = self.elements
        for i in range(self.elements):
            values[i] = self.get_value(input_stream)

        return values