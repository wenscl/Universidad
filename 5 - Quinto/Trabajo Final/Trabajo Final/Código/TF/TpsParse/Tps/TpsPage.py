from io import BytesIO, BufferedRandom
from TpsParse.Record.RecordManager import get_record
from TpsParse.Utils import BitUtil
from TpsParse.Utils.Decode import decode

class TpsPage:
    """
        The TpsPage holds TpsRecords, which may be compressed using Run Length 
        Encoding (RLE).
        There is no proper flag that signals if the page is compressed.
        Currently the page is thought of as compressed when the pageSize is different 
        from the uncompressedSize<i> and</i> the flags are 0x00. Some records with 
        the flag set to a non zero value also have different lengths, but the data 
        is not compressed..
        Building the TpsRecords out of the TpsPage uses also a custom compression 
        algorithm.
        As most headers of the TpsRecords are identical, some bytes can be saved by 
        reusing the headers of previous records. The first byte of each TpsRecord 
        indicates what parts should be reused. Obviously the first record on a page 
        should have a full header (0xC0).
    """
    
    def __init__(self, input_stream):
        buffer = BufferedRandom(BytesIO(input_stream.read(13)))

        self.addr = BitUtil.to_int32(buffer, 0)
        self.page_size = BitUtil.to_int16(buffer, 4)
        self.page_size_uncompressed = BitUtil.to_int16(buffer, 6)
        self.page_size_uncompressed_without_header = BitUtil.to_int16(buffer, 8)
        self.record_count = BitUtil.to_int16(buffer, 10)
        buffer.seek(12)
        self.flags = buffer.read()
        self._compressed_data = input_stream.read(self.page_size - 13)
        self.records = []
        self._data = None


    def _uncompress(self):
        if self.page_size != self.page_size_uncompressed and self.flags == bytes([0]):
            self._data = decode(self._compressed_data)
        else:
            self._data = self._compressed_data


    def _is_flushed(self):
        
        return self._data is None

    def flush(self):
        self._data = None
        self.records.clear()


    def parse_records(self):
        if self._is_flushed():
            self._uncompress()
        
        self.records.clear()
        # Skip pages with non 0x00 flags as they don't seem to contain TpsRecords.
        if self.flags == bytes([0]):
            stream = BytesIO(self._data)
            previous = None
            while stream.tell() != len(stream.getbuffer()) - 1 and \
                                        len(self.records) < self.record_count:
                current = get_record(stream, previous)
                self.records.append(current)
                previous = current