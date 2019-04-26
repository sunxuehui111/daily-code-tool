# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:10:06 2018

@author: ctrpg
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user=""    #用户名
mail_pass=""   #口令 
 
 
sender = '@163.com'
receivers = ['782180327@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('死亡轰炸', 'plain','utf-8')
message['From'] = sender
message['To'] =  '782180327@qq.com'
 
subject = 'Python SMTP 邮件'
message['Subject'] = Header(subject,'utf-8')
 
''' 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")'''
i = 30
while(i>0):
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
    i -= 1
