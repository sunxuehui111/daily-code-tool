# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:52:45 2018

@author: ctrpg
"""

# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
print (s.recv(1024))
s.send('I am client')
s.close()

