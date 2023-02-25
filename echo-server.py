# echo-server.py

import socket
import uuid
import codecs
import get_mac


# Next step is to pass the IP address of the host and listening port number

HOST = ""
PORT = 65432

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