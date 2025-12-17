import binascii

# PARITY BIT (EVEN)
def parity_bit(text):
    binary = ''.join(format(ord(c), '08b') for c in text)
    ones = binary.count('1')
    return '0' if ones % 2 == 0 else '1'


# 2D PARITY
def parity_2d(text):
    bits = [format(ord(c), "08b") for c in text]

    while len(bits) % 8 != 0:
        bits.append("00000000")

    matrix = [bits[i:i+8] for i in range(0, len(bits), 8)]

    row_parity = ""
    col_parity = ""

    for row in matrix:
        ones = ''.join(row).count("1")
        row_parity += '0' if ones % 2 == 0 else '1'

    for bit_pos in range(8):
        ones = 0
        for row in matrix:
            for byte in row:
                ones += int(byte[bit_pos])
        col_parity += '0' if ones % 2 == 0 else '1'

    return row_parity + col_parity


# CRC16
def crc16(text):
    crc = binascii.crc_hqx(text.encode(), 0xFFFF)
    return format(crc, '04X')


# HAMMING (DETECTION ONLY)
def hamming_code(text):
    encoded = ""
    for c in text:
        b = format(ord(c), "08b")
        d = [int(x) for x in b]
        p1 = d[0] ^ d[1] ^ d[3] ^ d[4] ^ d[6]
        p2 = d[0] ^ d[2] ^ d[3] ^ d[5] ^ d[6]
        p3 = d[1] ^ d[2] ^ d[3] ^ d[7]
        encoded += b + str(p1) + str(p2) + str(p3)
    return encoded


# INTERNET CHECKSUM
def internet_checksum(text):
    data = text.encode()
    if len(data) % 2 == 1:
        data += b'\x00'

    checksum = 0
    for i in range(0, len(data), 2):
        word = data[i] << 8 | data[i+1]
        checksum += word
        checksum = (checksum & 0xffff) + (checksum >> 16)

    checksum = ~checksum & 0xffff
    return format(checksum, '04X')
