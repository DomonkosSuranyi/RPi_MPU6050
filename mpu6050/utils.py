def bytes_to_word(high, low):
    val = (high << 8) + low
    if (val >= 0x8000):
        return -((65535 - val)+1)
    else:
        return val
