# -*- coding: utf-8 -*-
from socket import *

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

clientSocet = socket(AF_INET, SOCK_STREAM)
clientSocet.connect(ADDRESS)
while True:
    data = input('> ')
    if not data:
        break
    clientSocet.send(data.encode())
    data = clientSocet.recv(BUFFER).decode()
    if not data:
        break
    print(data)
clientSocet.close()
