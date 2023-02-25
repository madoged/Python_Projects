# echo-client.py

import socket
import codecs
import argparse

#Next step is to pass the host listening IP and port

parser = argparse.ArgumentParser(description="Reach out to server")
parser.add_argument("Host")
args = parser.parse_args()

HOST = args.Host
PORT = 65432

f = open("mymac.txt", "w")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hello, World")
    data = s.recv(1024)
    


print(f"Received {codecs.decode(data)!r}")
mac = str(data)
f.write(mac)
f.close()
