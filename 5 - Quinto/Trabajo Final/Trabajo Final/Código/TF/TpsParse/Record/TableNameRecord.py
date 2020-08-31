from TpsParse.Utils import BitUtil
from TpsParse.Tps.TpsRecord import TpsRecord
from io import BytesIO, BufferedRandom

class TableNameRecord(TpsRecord):
    def __init__(self, data, header):
        super().__init__(data, header, False)
        header = BytesIO(header)
        header.seek(1)
        to_decode = header.read(len(header.getvalue()) - 1)
        self.name = to_decode.decode("iso-8859-1")
        self.table_number = BitUtil.to_int32(BufferedRandom(BytesIO(data)), 0, False)