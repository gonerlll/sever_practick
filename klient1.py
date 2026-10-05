import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))
def mess_recv():
    buffer = b""
    while True:
        data = client.recv(1024)
        if not data:
            break
        buffer += data
        parts = buffer.split(b"\n")
        buffer = parts[-1]
        for part in parts[:-1]:
            print(part.decode())


thread = threading.Thread(target=mess_recv)
thread.start()
while True:
    mes = input("видите собщение")
    client.sendall((mes + "\n").encode())
    print("ведите сообщение!")