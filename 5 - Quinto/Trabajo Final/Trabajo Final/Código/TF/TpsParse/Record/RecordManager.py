from TpsParse.Utils import BitUtil
from TpsParse.Record import EmptyRecord, TableNameRecord, DataRecord, \
    MetadataRecord, TableDefinitionRecord, MemoRecord, IndexRecord
from construct import Int8ub
from io import BufferedRandom, BytesIO
from copy import copy as cp

def create_record(header, data):
    if len(header) < 5:
        return EmptyRecord.EmptyRecord(data, header)

    if header[0] == 0xFE:
        return TableNameRecord.TableNameRecord(data, header)

    if header[4] == 0xF3:
        return DataRecord.DataRecord(data, header)
    elif header[4] == 0xF6:
        return MetadataRecord.MetadataRecord(data, header)
    elif header[4] == 0xFA:
        return TableDefinitionRecord.TableDefinitionRecord(data, header)
    elif header[4] == 0xFC:
        return MemoRecord.MemoRecord(data, header)
    else:
        return IndexRecord.IndexRecord(data, header)


def get_record(input_stream, previous=None):
    if previous is None:
        buffer = input_stream.read(5)

        flags = buffer[0]
        if (flags & 0xC0) != 0xC0:
            raise Exception(f'Can\'t construct a TpsRecord without record '
                            f'lengths (0x{flags}).')

        _buffer = BufferedRandom(BytesIO(buffer))
        record_length = BitUtil.to_int16(_buffer, 1)
        header_length = BitUtil.to_int16(_buffer, 3)

        header = input_stream.read(header_length)
        data = input_stream.read(record_length - header_length)

        return create_record(header, data)

    else:
        flags = Int8ub.parse(input_stream.read(1))

        if (flags & 0x80) != 0:
            buffer = BufferedRandom(BytesIO(input_stream.read(2)))
            record_length = BitUtil.to_int16(buffer, 0)
        else:
            record_length = len(previous.data) + len(previous.header)

        if (flags & 0x40) != 0:
            buffer = BufferedRandom(BytesIO(input_stream.read(2)))
            header_length = BitUtil.to_int16(buffer, 0)
        else:
            header_length = len(previous.header)

        copy = flags & 0x3F
        all_data = bytes(record_length)
        try:
            if copy > 0:
                pos = len(previous.header) if copy > len(previous.header) \
                    else copy
                all_data = cp(previous.header[:pos])

                if copy > len(previous.header):
                    all_data[len(previous.header):] = \
                        cp(previous.data[:copy - len(previous.header)])

            all_data = BytesIO(all_data)
            all_data.seek(copy)
            all_data.write(input_stream.read(record_length - copy))

        except Exception as e:
            raise Exception(f'When reading {record_length - copy} bytes of '
                            f'TpsRecord at {input_stream.tell()}. {e}')

        all_data = all_data.getvalue()
        header = cp(all_data[:header_length])
        data = cp(all_data[header_length:])

        return create_record(header, data)