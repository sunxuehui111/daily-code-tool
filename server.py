# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:52:07 2018

@author: ctrpg
"""

# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("连接地址: %s" % str(addr))
    msg='欢迎访问！'+ "\r\n"
    if clientsocket.send(msg):
        print(clientsocket.recv(1024))
    clientsocket.close()