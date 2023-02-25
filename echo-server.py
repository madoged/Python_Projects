# echo-server.py

"""
Homework:
main() - check
argparse - check

I lost and forgot how we formatted the mac address
I kind of cheated but I learned how to split a string into a list and rejoin it, so there is that.

Extra credit - read port number on server side from file and write mac on client side to a file
"""

import socket
import codecs
import get_mac

file = open("text.txt", "r")
s = file.read()
PORT = int(s)
file.close()

HOST = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST,PORT))
    s.listen()
    print("Listening...")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        MAC = get_mac.get_mac()
        while True:
            data = conn.recv(1024)
            print(f"This is the message from client: {data}") #print the message before sending it back
            if not data:
                break
            conn.sendall(codecs.encode(MAC))