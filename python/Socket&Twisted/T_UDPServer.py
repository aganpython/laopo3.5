# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

udpSocket = socket(AF_INET, SOCK_DGRAM)  # 创建服务端socket
udpSocket.bind(ADDRESS)

while True:
    print('等待连接......')
    data, addr = udpSocket.recvfrom(BUFFER)
    print(data.decode())
    udpSocket.sendto(('[%s] %s' % (ctime(), data.decode())).encode(), addr)
    print('返回给：', addr)

udpSocket.close()
