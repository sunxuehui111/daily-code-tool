# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:39:54 2018

@author: ctrpg
"""
'''
from urllib import request
response = request.urlopen("http://www.9vf.com/")  # 打开网站
fi = open("新建文本文档.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件
'''


#修改文件名
'''
import os
path=input('请输入文件路径(结尾加上/)：')       

#获取该目录下所有文件，存入列表中
f=os.listdir(path)

n=0
for i in f:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+f[n]
    
    #设置新文件名
    newname=path+'b'+str(n+1)+'.txt'
    
    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    
    n+=1'''
    



