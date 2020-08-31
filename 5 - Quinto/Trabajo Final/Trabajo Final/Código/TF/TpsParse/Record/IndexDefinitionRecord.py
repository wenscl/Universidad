from TpsParse.Utils import BitUtil

class IndexDefinitionRecord:
    def __init__(self, input_stream):
        self.external_file = BitUtil.zero_terminated_string(input_stream)

        if len(self.external_file) == 0:
            if input_stream.read(1) != bytes([1]):
                raise Exception("Bad Index Definition, missing 0x01 after zero string.")

        self.name = BitUtil.zero_terminated_string(input_stream)
        self.flags = input_stream.read(1)
        self.fields_in_key = BitUtil.stream_to_int16(input_stream)
        self.key_field = [0]*self.fields_in_key
        self.key_field_flag = [0]*self.fields_in_key

        for i in range(self.fields_in_key):
            self.key_field[i] = BitUtil.stream_to_int16(input_stream)
            self.key_field_flag[i] = BitUtil.stream_to_int16(input_stream)


    def get_field_records(self, record):
        results = []
        for i in range(len(self.key_field)):
            results.append(record.fields[i])
        
        return results