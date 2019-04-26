# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:00:48 2018

@author: ctrpg
"""
'''import re

carnum = input("请输入车牌：");

num =  re.sub("\D","", str)

getLastNum = int(num[len(num) - 1])

limitNum = [[1,6],[2,7],[3,8],[4,9],[5,0]]

if getLastNum in limitNum[0]:
	print("该车牌周一限行")

elif getLastNum in limitNum[1]:
	print("该车牌周二限行")

elif getLastNum in limitNum[2]:
	print("该车牌周三限行")

elif getLastNum in limitNum[3]:
	print("该车牌周四限行")

else:
	print("该车牌周五限行")'''


#生日
'''忽略2月，默认每月31天'''
import random

#随机生成23个生日
def rand_birth():
    birthday = []
    for i in range(23):
        month = str(random.randint(1,12))
        day = str(random.randint(1,31))
        birthday.append(month + '-' + day)
    return birthday
#判断生日相同个数
def all_list(arr):
    counter = 0
    for i in set(arr):
        if(arr.count(i)>1):
            counter += arr.count(i)
    return counter

num = int(input("请输入班级个数："))
allsame = 0;
allnum = num * 23
while(num>0):
    buf = rand_birth()
    allsame += all_list(buf)
    num -= 1
print("概率为：" , allsame/allnum)




    
    
'''# 知道是该年第几天
import time
p = [31,28,31,30,31,30,31,31,30,31,30,31] # 平年
w = [31,29,31,30,31,30,31,31,30,31,30,31] # 闰年

year =time.localtime().tm_year
month =time.localtime().tm_mon
day=time.localtime().tm_mday

arr=[31,28,31,30,31,30,31,31,30,31,30,31]
sum=day
for i in range(0,month-1):
    sum+=arr[i]
if year%4==0:
    if year%100==0 and year%400!=0:
        print ("这是今年的第%d天" % sum)
    else:
        sum=sum+1
        print ("这是今年的第%d天" % sum)
else: 
    print ("这是今年的第%d天" % sum)'''
    
#水仙花
'''for i in range(100, 1000):
    s = str(i)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == i:
        print(i)'''
#斐波那契
'''import sys

def fibonacci(n,w=0): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(100,0) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except :
        sys.exit()'''
    
#lambda作业
    
'''s = "Sorting1234"
 
s ="".join(sorted(s, key=lambda x: (x.islower(), x.isupper(),x.isdigit(), x.isdigit() and int(x) % 2 == 0, x)))
print(s)'''
'''import re
import os 
def read_file_as_str(file_path): # 判断路径文件存在 
    if not os.path.isfile(file_path): 
        raise TypeError(file_path + " does not exist") 
    all_the_text = open(file_path).read()  
    #print (type(all_the_text))
    return all_the_text
def all_list(arr):
    result = {}
    for i in set(arr):
        if(arr.count(i)>1):
            result[i] = arr.count(i)
    return result
fileadr = os.getcwd()
filefull = fileadr + "\唐诗三百首.txt"
resultstr = read_file_as_str(filefull)
bufstr = ''.join(re.findall(u'[\u4e00-\u9fff]+', resultstr))
reslut = all_list("".join(bufstr.split()))
print(sorted(reslut.items(),key = lambda x:x[1],reverse = True))'''


