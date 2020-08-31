from enum import Enum

class FieldType(Enum):
    Byte = bytes([1]),
    SignedShort = bytes([2]),
    UnsignedShort = bytes([3]),
    Date = bytes([4]),
    Time = bytes([5]),
    SignedLong = bytes([6]),
    UnsignedLong = bytes([7]),
    Float = bytes([8]),
    Double = bytes([9]),
    Bcd = bytes([10]),
    FixedLengthString = bytes([18]),
    ZeroTerminatedString = bytes([19]),
    PascalString = bytes([20]),
    Group = bytes([22])