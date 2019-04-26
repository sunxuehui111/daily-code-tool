# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:45:54 2019

@author: ctrpg
"""
from xlutils.copy import copy
import xlrd,xlwt
name = ''
__all__=[ ]
def createInitExcel(address,projectname):
    name = projectname
    book = xlwt.Workbook()#新建一个excel对象
    sheet = book.add_sheet(projectname)#添加一个sheet页
    sheet.write_merge(0, 0, 0, 6, projectname)
    book.save(name)#写excel的时候，你保存的文件名必须是xls
    
def headerExcel(aname,index):
    book = xlrd.open_workbook(name)
    new_book = copy(book) #通过xlutils里面copy复制一个excel对旬
    sheet = new_book.get_sheet(0) #获取sheet页
    title = ['序号','项目名称','单位','数量','单价','小计','备注']
    for i in range(len(title)):
        #title多长，循环几次
        sheet.write(index,i,title[i])
        #i既是lis的下标，也代表每一列#处理表头
        #sheet.write(0,0,title) #将内容写到excel
    book.save(name)#写excel的时候，你保存的文件名必须是xls


def insertExecl(siglenum,projectname,unit,countnum,unitprice,price,note,index):
    book = xlrd.open_workbook(name)
    new_book = copy(book) #通过xlutils里面copy复制一个excel对旬
    sheet = new_book.get_sheet(0) #获取sheet页
    sheet.write(index,0,siglenum)#写入修改的内容
    sheet.write(index,1,projectname)#写入修改的内容
    sheet.write(index,2,unit)#写入修改的内容
    sheet.write(index,3,countnum)#写入修改的内容
    sheet.write(index,4,unitprice)#写入修改的内容
    sheet.write(index,5,price)#写入修改的内容
    sheet.write(index,6,note)#写入修改的内容
    new_book.save(name) #保存excel