import socket
import threading
import time


start = time.time()
def scan_port(addr,port):

    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan.settimeout(0.5)
    result = scan.connect_ex((addr, port))
    if result == 0:
        print(port,"открыт")
        open_Ports.append(port)
    scan.close()
potoc =[]
open_Ports=[]
addr = input("видите ситивой адресс")
bol = True
while bol == True:
    start_scan = int(input("ведите начальноый порт"))
    end_scan = int(input("видите конечный порт"))
    if start_scan > end_scan:
        print("вы вели началюну. суму большн конечной")
    else:
        bol = False

for i in range(start_scan,end_scan+1):

    thread = threading.Thread(target=scan_port, args=(addr,i))
    potoc.append(thread)
    thread.start()


for i in potoc:
   i.join()
end = time.time()
print(sorted(open_Ports))
print(end-start)












# start = time.time()
# for i in range(8000,8085):
#     scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     scan.settimeout(0.5)
#     result = scan.connect_ex(("127.0.0.1",i))
#     if result == 0:
#         print(i,":открыто")
#     scan.close()
# end = time.time()
# print(end-start)