from TpsParse.Tps.TpsHeader import TpsHeader
from TpsParse.Tps.TpsBlock import TpsBlock
from TpsParse.Record.TableDefinitionRecord import TableDefinitionRecord
from TpsParse.Record.TableNameRecord import TableNameRecord
from TpsParse.Record.DataRecord import DataRecord

class TpsFile:
    """
        Construct a new TpsFile from the given stream.
    """
    def __init__(self, input_stream):
        # "input_stream" = Stream containing the TPS file.
        # The stream must be seekable.
        if not input_stream.seekable():
            raise OSError('The tps file must be seekable.')

        self._input_stream = input_stream
        input_stream.seek(0, 0)
        self.file_size = len(input_stream.read())

    # Read the header of the TPS file.
    def get_header(self):
        self._input_stream.seek(0, 0)

        header = TpsHeader(self._input_stream)
        if not header.is_top_speed_file():
            raise Exception("Not a TopSpeed file")

        return header

    # Get the blocks from the TPS file.
    def get_tps_blocks(self):
        header = self.get_header()
        blocks = []
        for t in range(len(header.page_start)):
            ofs = header.page_start[t]
            end = header.page_end[t]

            # Skips the first entry (0 length) and any blocks that are beyond
            # the file size.
            if not (ofs == 0x0200 and end == 0x200) and ofs < self.file_size:
                blocks.append(TpsBlock(self._input_stream, ofs, end, self.file_size))
                
        return blocks

    # Get all the records in a file.
    def get_all_records(self):
        records = []
        for block in self.get_tps_blocks():
            for page in block.pages:
                page.parse_records()
                records.extend(page.records)
        
        return records

    # Get a list of table definitions in the file.
    # Generally, most files will have a single table.
    def get_table_definitions(self):
        table_map = {}
        for record in self.get_all_records():
            if isinstance(record, TableDefinitionRecord):
                if record.table_number in table_map:
                    table_map[record.table_number].append(record)
                else:
                    table_map[record.table_number] = [record]

        records = []
        for key, value in table_map.items():
            definition = TableDefinitionRecord.merge(value)
            definition.parse_data()
            records.append(definition)

        return records

    # Get table name.
    def get_table_name(self):
        records = []
        for record in self.get_all_records():
            if isinstance(record, TableNameRecord):
                records.append(record)
        return records

    # Get a list of data records in the file.
    def get_data_records(self, table_definition):
        records = []
        for record in self.get_all_records():
            if isinstance(record, DataRecord):
                if record.table_number == table_definition.table_number:
                    record.parse_values(table_definition)
                    records.extend([record])

        return records