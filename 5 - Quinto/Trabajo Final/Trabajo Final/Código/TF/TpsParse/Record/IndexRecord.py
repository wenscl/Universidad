from TpsParse.Tps.TpsRecord import TpsRecord

class IndexRecord(TpsRecord):
    def __init__(self, data, header):
        super().__init__(data, header, True)
        self.index_number = header[4]