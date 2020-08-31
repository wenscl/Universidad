from TpsParse.Tps.TpsRecord import TpsRecord

class MetadataRecord(TpsRecord):
    def __init__(self, data, header):
        super().__init__(data, header, True)
        self.about_type = header[5]


    def is_about_key_or_index(self):
        return self.about_type < 0xF3