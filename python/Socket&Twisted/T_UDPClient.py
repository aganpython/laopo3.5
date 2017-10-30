# -*- coding: utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 10001
BUFFER = 1024

ADDRESS = (HOST, PORT)

udpClient = socket(AF_INET, SOCK_DGRAM)  # 创建客户端socket

while True:
    data = input('> ')
    if not data:
        break
        udpClient.sendto(data.encode(), ADDRESS)
    data, ADDRESS = udpClient.recvfrom(BUFFER)
    if not data:
        break
    print(data.decode())
    print(ADDRESS)

udpSocket.close()
