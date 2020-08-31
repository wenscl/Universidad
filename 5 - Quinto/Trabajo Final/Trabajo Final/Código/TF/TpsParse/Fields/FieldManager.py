from TpsParse.Fields import BcdField, ByteField, DateField, DoubleField, \
    FixedLengthStringField, FloatField, GroupField, PascalStringField, \
    SignedLongField, SignedShortField, TimeField, UnsignedLongField, \
    UnsignedShortField, ZeroTerminatedStringField
from TpsParse.Utils.FieldType import FieldType


class FieldManager:
    # Get the value of this field.
    # Returns an object representing the value based on the type of the field.
    @staticmethod
    def get_field(input_stream):
        field_type = input_stream.read(1)

        if field_type == FieldType.Bcd.value[0]:
            field = BcdField.BcdField(input_stream)
        elif field_type == FieldType.Byte.value[0]:
            field = ByteField.ByteField(input_stream)
        elif field_type == FieldType.Date.value[0]:
            field = DateField.DateField(input_stream)
        elif field_type == FieldType.Double.value[0]:
            field = DoubleField.DoubleField(input_stream)
        elif field_type == FieldType.FixedLengthString.value[0]:
            field = FixedLengthStringField.FixedLengthStringField(input_stream)
        elif field_type == FieldType.Float.value[0]:
            field = FloatField.FloatField(input_stream)
        elif field_type == FieldType.Group.value[0]:
            field = GroupField.GroupField(input_stream)
        elif field_type == FieldType.PascalString.value[0]:
            field = PascalStringField.PascalStringField(input_stream)
        elif field_type == FieldType.SignedLong.value[0]:
            field = SignedLongField.SignedLongField(input_stream)
        elif field_type == FieldType.SignedShort.value[0]:
            field = SignedShortField.SignedShortField(input_stream)
        elif field_type == FieldType.Time.value[0]:
            field = TimeField.TimeField(input_stream)
        elif field_type == FieldType.UnsignedLong.value[0]:
            field = UnsignedLongField.UnsignedLongField(input_stream)
        elif field_type == FieldType.UnsignedShort.value[0]:
            field = UnsignedShortField.UnsignedShortField(input_stream)
        elif field_type == FieldType.ZeroTerminatedString.value[0]:
            field = ZeroTerminatedStringField.ZeroTerminatedStringField(input_stream)
        else:
            raise Exception(f'The field type {field_type} is not implemented.')

        return field
