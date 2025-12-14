import socket
import random

# ================= ERROR INJECTION =================

def bit_flip(data):
    i = random.randint(0, len(data)-1)
    return data[:i] + chr(ord(data[i]) ^ 1) + data[i+1:]

def char_sub(data):
    i = random.randint(0, len(data)-1)
    return data[:i] + chr(random.randint(65, 90)) + data[i+1:]

def char_del(data):
    i = random.randint(0, len(data)-1)
    return data[:i] + data[i+1:]

def char_insert(data):
    i = random.randint(0, len(data))
    return data[:i] + chr(random.randint(97,122)) + data[i:]

def swap(data):
    if len(data) < 2:
        return data
    i = random.randint(0, len(data)-2)
    lst = list(data)
    lst[i], lst[i+1] = lst[i+1], lst[i]
    return ''.join(lst)

def burst_error(data):
    if len(data) < 5:
        return data
    start = random.randint(0, len(data)-5)
    end = start + random.randint(3,5)
    return data[:start] + ''.join(chr(random.randint(33,126)) for _ in range(end-start)) + data[end:]

corrupt_methods = [bit_flip, char_sub, char_del, char_insert, swap, burst_error]

# ================= SERVER =================

def server():
    s = socket.socket()
    s.bind(("localhost", 9999))
    s.listen()

    print("Server running...")
    conn, addr = s.accept()
    print("Connected:", addr)

    packet = conn.recv(2048).decode()
    print("Received:", packet)

    data, method, control = packet.split("|", 2)

    corrupt = random.choice(corrupt_methods)

    if method == "HAMMING":
        control = corrupt(control)
    else:
        data = corrupt(data)

    new_packet = f"{data}|{method}|{control}"
    print("Forwarded packet:", new_packet)

    conn2 = socket.socket()
    conn2.connect(("localhost", 10000))
    conn2.send(new_packet.encode())

    conn.close()
    conn2.close()


if __name__ == "__main__":
    server()
