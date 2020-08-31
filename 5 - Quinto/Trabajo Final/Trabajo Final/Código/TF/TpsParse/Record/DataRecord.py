from TpsParse.Utils import BitUtil
from io import BytesIO, BufferedRandom
from TpsParse.Tps.TpsRecord import TpsRecord

class DataRecord(TpsRecord):
    def __init__(self, data, header):
        super().__init__(data, header, True)
        self.record_number = BitUtil.to_int32(BufferedRandom(BytesIO(header)), 5, False)

    # To parse the values in a field, you must pass the table definition.
    # "record"=Table definition of the data field.
    def parse_values(self, record):
        self.values = []
        stream = BytesIO(self.data)
        for field in record.fields:
            if field.is_array():
                self.values.append(field.get_array_value(stream))
            else:
                self.values.append(field.get_value(stream))