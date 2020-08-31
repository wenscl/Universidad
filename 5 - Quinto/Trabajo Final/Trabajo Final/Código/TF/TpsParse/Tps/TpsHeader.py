from TpsParse.Utils import BitUtil
from io import BufferedRandom, BytesIO

class TpsHeader:
    """
        TpsHeader represents the first 0x200 bytes of a TPS file.
        Aside from the 'tOpS' identifier, it holds an array of page addresses and other meta information.
    """
    def __init__(self, input_stream):
        input_stream.seek(0, 0)
        buffer = BufferedRandom(BytesIO(input_stream.read(0x200)), buffer_size=0x200)

        self.addr = BitUtil.to_int16(buffer, 0)
        self.hdr_size = BitUtil.to_int16(buffer, 4)
        self.file_length_1 = BitUtil.to_int32(buffer, 6)
        self.file_length_2 = BitUtil.to_int32(buffer, 10)
        self.zeros = BitUtil.to_int16(buffer, 18)
        self.last_issued_row = BitUtil.to_int32(buffer, 20)
        self.changes = BitUtil.to_int32(buffer, 24)
        self.management_page_ref = BitUtil.to_int32(buffer, 28)
        self.page_start = self.get_int32_array(buffer, 32, 60)
        self.page_end = self.get_int32_array(buffer, 272, 60)
        
        buffer.seek(14, 0)
        buffer = buffer.read(4)
        try:
            self.top_speed = buffer.decode('ascii')
        except UnicodeDecodeError:
            raise UnicodeDecodeError
    
    @staticmethod
    def get_int32_array(buffer, start_index, length):
        result = []
        for i in range(length):
            result.append((BitUtil.to_int32(buffer, start_index + (i * 4)) << 8) + 0x200)
        
        return result


    def is_top_speed_file(self):
        return self.top_speed == "tOpS"