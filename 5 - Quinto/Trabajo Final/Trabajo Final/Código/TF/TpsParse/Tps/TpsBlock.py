from TpsParse.Utils import BitUtil
from TpsParse.Tps.TpsPage import TpsPage

class TpsBlock:
    """
        A TpsBlock is the outermost container for data, it groups a number of TpsPages.
        As far as I know a TpsBlock holds no information about the TpsPages it contains.
        Currently the pages are identified by scanning for them.
        The current algorithm works by beginning at the block start,
        parsing the TpsPage and then seeking for the next TpsPage using its
        offset in the file(always at a 0x0100 boundary and the value at that
        address must have the same value as the offset). Far from perfect but
        it seems to work.
    """

    def __init__(self, input_stream, start, end, file_size):
        self.pages = []

        input_stream.seek(start)

        while input_stream.tell() < end:
            self.pages.append(TpsPage(input_stream))

            if (input_stream.tell() & 0xFF) == 0:
                # Actually we might be already at a new page.
                pass
            else:
                # Jump to the next probable page.
                input_stream.seek((input_stream.tell() & 0xFFFFFF00) + 0x0100)
            
            addr = 0
            while addr != input_stream.tell() and input_stream.tell() < file_size - 1:
                addr = BitUtil.stream_to_int32(input_stream)
                input_stream.seek(-4, 1)

                # check if there is really a page here.
                # if so, the offset in the file must match the value.
                # if not, we continue.
                if addr != input_stream.tell():
                    input_stream.seek(0x1000 - 4, 1)


    def flush(self):
        for page in self.pages:
            page.flush()