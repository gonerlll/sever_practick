import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))
def mess_recv():
    buffer = b""
    while True:
        try:
            data = client.recv(1024)
        except OSError as e:
            print(e)
            break

        if not data:
            break
        buffer += data
        parts = buffer.split(b"\n")
        buffer = parts[-1]
        for part in parts[:-1]:
            print(part.decode())


thread = threading.Thread(target=mess_recv,daemon=True)
thread.start()
while True:
    mes = input("видите собщение")
    try:
        client.sendall((mes + "\n").encode())
    except OSError as e:
        print(f"ошибка {e} ")
        break
