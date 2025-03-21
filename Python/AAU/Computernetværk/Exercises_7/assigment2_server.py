from socket import *
import sys

Host = ''
PORT = 9999
BUFSIZE = 1024
s = socket(AF_INET, SOCK_STREAM)
s.bind((Host, PORT))

while True:
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(BUFSIZE)
    if not data or data == b'exit':
        break
    match(data):
        case b'file':
            conn.sendall(b'Hello, World!')
        case b'query':
            conn.sendall(b'Goodbye, World!')
        case _:
            conn.sendall(b'Invalid option!')