from io import BufferedRandom, BytesIO

def decode(data):
    """
        Handles the RLE (run length encoding) decoding.
    """
    _data = BufferedRandom(BytesIO(data))
    output = BufferedRandom(BytesIO())
    try:
        pos = 0
        while pos < len(data) - 1:
            skip = data[pos]
            pos += 1

            if skip == 0:
                raise Exception("Bad RLE Skip (0x00)")

            if skip > 0x7F:
                msb = data[pos]
                pos += 1
                lsb = (skip & 0x7F)
                shift = 0x80 * (msb & 0x01)
                skip = ((msb << 7) & 0x00FF00) + lsb + shift

            _data.seek(pos)
            to_write = _data.read(skip)
            output.write(to_write)
            pos += skip

            if pos >= len(data):
                break

            to_repeat = bytes([data[pos - 1]])
            repeats_minus_one = data[pos]
            pos += 1

            if repeats_minus_one > 0x7F:
                msb = data[pos]
                pos += 1
                lsb = (repeats_minus_one & 0x7F)
                shift = 0x80 * (msb & 0x01)
                repeats_minus_one = ((msb << 7) & 0x00FF00) + lsb + shift

            for _ in range(repeats_minus_one):
                output.write(to_repeat)
    except IOError as e:
        raise Exception(f"Error while RLE decoding. {e}")

    output.seek(0)

    return output.read()