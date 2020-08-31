from TpsParse.Tps.TpsRecord import TpsRecord

class EmptyRecord(TpsRecord):
    def __init__(self, data, header):
        super().__init__(data, header, False)