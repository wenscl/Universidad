from TpsParse.Utils import BitUtil
from io import BytesIO, BufferedRandom

class TpsRecord:
    def __init__(self, data, header, read_table):
        self.data = data
        self.header = header
        if read_table:
            self.table_number = BitUtil.to_int32(BufferedRandom(BytesIO(header)), 0, False)