from TpsParse.Utils import BitUtil
from TpsParse.Tps.TpsRecord import TpsRecord
from io import BytesIO, BufferedRandom

class MemoRecord(TpsRecord):
    def __init__(self, data, header):
        super().__init__(data, header, True)
        self.owning_record = BitUtil.to_int32(BufferedRandom(BytesIO(header)), 5, False)
        self.memo_index = header[9]
        self.sequence_number = BitUtil.to_int16(BufferedRandom(BytesIO(header)), 10, False)