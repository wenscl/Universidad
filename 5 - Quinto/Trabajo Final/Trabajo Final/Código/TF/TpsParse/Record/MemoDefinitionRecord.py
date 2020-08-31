from TpsParse.Utils import BitUtil

class MemoDefinitionRecord:
    def __init__(self, input_stream):
        self.external_file = BitUtil.zero_terminated_string(input_stream)

        if len(self.external_file) == 0:
            if input_stream.read(1) != bytes([1]):
                raise Exception("Bad Memo Definition, missing 0x01 after zero string.")

        self.name = BitUtil.zero_terminated_string(input_stream)
        self.length = BitUtil.stream_to_int16(input_stream)
        self.flags = BitUtil.stream_to_int16(input_stream)


    def is_memo(self):

        return (self.flags & 0x04) == 0


    def is_blob(self):

        return (self.flags & 0x04) != 0