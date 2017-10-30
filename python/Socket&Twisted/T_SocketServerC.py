# -*- coding: utf-8 -*-


from socket import *

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

while True:
    tcpClientSocet = socket(AF_INET, SOCK_STREAM)
    tcpClientSocet.connect(ADDRESS)

    data = input('> ')
    if not data:
        break
    tcpClientSocet.send(('%s\r\n' % data).encode())
    data = tcpClientSocet.recv(BUFFER)
    if not data:
        break
    print(data.strip().decode())
tcpClientSocet.close()
