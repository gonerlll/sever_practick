import socket
import time
import threading


def scan_port(addr,port):
    scan = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    scan.settimeout(0.5)
    resultat = scan.connect_ex((addr,port))
    if resultat == 0:
        print(port)
        open_ports.append(port)
    scan.close()

while True :
    try:
        start = int(input("нвчвльное число"))
        end = int(input("конечное число"))
        if end >65535 or start <= 0 :
            print("порты видены не коректно")
            continue

    except ValueError:
        print("ведите числа")
        continue
    if start > end:
        print("начальное число больше канечного")
        continue
    break
open_ports = []
th = []

adr = input("видите ситивой адресс")
startt = time.time()
for i in range(start,end+1):

    thread = threading.Thread(target=scan_port, args=(adr,i,))
    th.append(thread)
    thread.start()


for t in th:
    t.join()

endt = time.time()
print(sorted(open_ports))
print(endt-startt)