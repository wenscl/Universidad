from construct import Int32sn, Int32sl, Int32sb, Int32un, Int32ul, Int32ub, \
    Int16sb, Int16sl, Int16sn, Int16ub, Int16ul, Int16un, Int8ub
from io import BytesIO


def to_int32(buffer, offset=None, little_endian=None):
    if offset is not None:
        buffer.seek(offset)

    if little_endian is None:
        return Int32sn.parse(buffer.read())
    elif little_endian:
        return Int32sl.parse(buffer.read())
    else:
        return Int32sb.parse(buffer.read())


def to_int32u(buffer, offset=None, little_endian=None):
    if offset is not None:
        buffer.seek(offset)

    if little_endian is None:
        return Int32un.parse(buffer.read())
    elif little_endian:
        return Int32ul.parse(buffer.read())
    else:
        return Int32ub.parse(buffer.read())


def to_int16(buffer, offset=None, little_endian=None):
    if offset is not None:
        buffer.seek(offset)

    if little_endian is None:
        return Int16sn.parse(buffer.read())
    elif little_endian:
        return Int16sl.parse(buffer.read())
    else:
        return Int16sb.parse(buffer.read())


def to_int16u(buffer, offset=None, little_endian=None):
    if offset is not None:
        buffer.seek(offset)

    if little_endian is None:
        return Int16un.parse(buffer.read())
    elif little_endian:
        return Int16ul.parse(buffer.read())
    else:
        return Int16ub.parse(buffer.read())


def zero_terminated_string(stream):
    string = BytesIO()
    b = Int8ub.parse(stream.read(1))
    while b != 0:
        string.write(bytes([b]))
        b = Int8ub.parse(stream.read(1))

    return string.getvalue().decode("iso-8859-1")


def stream_to_int16(stream):
    return to_int16(BytesIO(stream.read(2)), 0, True)


def stream_to_int16u(stream):
    return to_int16u(BytesIO(stream.read(4)), 0, True)


def stream_to_int32(stream):
    return to_int32(BytesIO(stream.read(4)), 0, True)


def stream_to_int32u(stream):
    return to_int32u(BytesIO(stream.read(4)), 0, True)