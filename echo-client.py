# echo-client.py

import socket
import codecs
import argparse

#Next step is to pass the host listening IP and port

HOST = ""
PORT = 65432

parser = argparse.ArgumentParser()
parser.add_argument("Host")
args = parser.parse_args()

target = Path(args.HOST)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hello, World")
    data = s.recv(1024)

print(f"Received {codecs.decode(data)!r}")