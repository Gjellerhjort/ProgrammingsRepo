import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12346))
server.listen(5) # listen for 5 connections
 
while True:
    client, addr = server.accept()
    print("Connection from: ", addr)
    buf = client.recv(64)
    if len(buf) > 0:
        print(buf)
        break
    client.close()