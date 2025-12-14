import socket
from client1 import parity_bit, parity_2d, crc16, hamming_code, internet_checksum

def client2():
    s = socket.socket()
    s.bind(("localhost", 10000))
    s.listen()

    print("Client2 waiting...")
    conn, addr = s.accept()

    packet = conn.recv(2048).decode()
    data, method, received = packet.split("|", 2)

    print("Received Data:", data)
    print("Method:", method)
    print("Sent Check Bits:", received)

    if method == "PARITY":
        computed = parity_bit(data)
    elif method == "PARITY2D":
        computed = parity_2d(data)
    elif method == "CRC16":
        computed = crc16(data)
    elif method == "HAMMING":
        computed = hamming_code(data)
    else:
        computed = internet_checksum(data)

    print("Computed Check Bits:", computed)

    if received == computed:
        print("Status: DATA CORRECT")
    else:
        print("Status: DATA CORRUPTED")

    conn.close()


if __name__ == "__main__":
    client2()
