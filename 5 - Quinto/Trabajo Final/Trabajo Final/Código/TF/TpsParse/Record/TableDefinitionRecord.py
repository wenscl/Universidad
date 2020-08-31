from TpsParse.Utils import BitUtil
from TpsParse.Fields.FieldManager import FieldManager
from TpsParse.Record.MemoDefinitionRecord import MemoDefinitionRecord
from TpsParse.Record.IndexDefinitionRecord import IndexDefinitionRecord
from io import BytesIO, BufferedRandom
from TpsParse.Tps.TpsRecord import TpsRecord

class TableDefinitionRecord(TpsRecord):
    def __init__(self, data, header):
        super().__init__(data, header, True)
        self.block = BitUtil.to_int16(BufferedRandom(BytesIO(header)), 5, False)
        self._data = data

    # This should only be called once table definitions are merged.
    def parse_data(self):
        stream = BytesIO(self._data)

        self.driver_version = BitUtil.stream_to_int16(stream)
        self.record_length = BitUtil.stream_to_int16(stream)
        self.number_of_fields = BitUtil.stream_to_int16(stream)
        self.number_of_memos = BitUtil.stream_to_int16(stream)
        self.number_of_indexes = BitUtil.stream_to_int16(stream)

        self.fields = []
        self.memos = []
        self.indexes = []

        try:
            for _ in range(self.number_of_fields):
                self.fields.append(FieldManager.get_field(stream))

            for _ in range(self.number_of_memos):
                self.memos.append(MemoDefinitionRecord(stream))

            for _ in range(self.number_of_indexes):
                self.indexes.append(IndexDefinitionRecord(stream))

        except Exception as e:
            raise Exception(f"Bad Table Definition. {e}")

    @staticmethod
    def merge(records):
        data = BytesIO()
        for record in records:
            data.write(record.data)

        return TableDefinitionRecord(data.getbuffer(), records[0].header)