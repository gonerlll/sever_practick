import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen()
client_number = 0
clients =[]
print("START")
def broadcast(messenge,sender):
    for client in clients:
        if client != sender:
            try:
                client.sendall(messenge.encode() + b"\n")
            except OSError:
                print("не удалось отправить")




def client_thread(conn,number):
    buffer = b""
    while True:
        try:
            data = conn.recv(1024)
        except ConnectionResetError:
            data = b""
        if not data:
            print(f"Client {number} disconnected")
            clients.remove(conn)
            mes = f"клиент {number} disconnected"
            broadcast(mes, conn)
            print(f"подключегтт осталось{len(clients)}")
            conn.close()
            break
        buffer += data
        parts = buffer.split(b"\n")
        buffer = parts[-1]
        for mes in parts[:-1]:
            messenge = f"klient {number}:{mes.decode()}"
            broadcast(messenge, conn)



while True:
    conn, addr = server.accept()
    client_number += 1
    clients.append(conn)
    print(f"Client {client_number} connected")
    print(f"всего {client_number} подключении")
    thread = threading.Thread(
        target=client_thread,daemon=True,
        args=(conn, client_number)
    )
    thread.start()


