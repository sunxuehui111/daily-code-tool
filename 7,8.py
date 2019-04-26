# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 09:35:42 2018

@author: ctrpg
"""



'''class Employee:
   '所有员工的基类'
   def __init__(self, name, pay):
      self.name = name
      self.pay = pay

 
   def get_last_name(self):
      return self.name
  
   def pay_raise(self,pay_persent):
      self.pay = self.pay * (1 + pay_persent)
  
if __name__=="__main__":
    ZhangSan=Employee('张三',8000)
    print(ZhangSan.get_last_name())
    ZhangSan.pay_raise(0.1)
    print(ZhangSan.pay)
    Dongfangbubai=Employee('东方不败',5000)
    print(Dongfangbubai.get_last_name())
    Dongfangbubai.pay_raise(-0.2)
    print(Dongfangbubai.pay)'''
    
    
    
    
class Manager:
    level = "初级" #初级为0， 高级为1
    def __init__(self, name, pay,level):
      self.name = name
      self.pay = pay
      self.level = level
    def get_last_name(self):
      return self.name
  
    def pay_raise(self,pay_persent):
      if self.level == "初级":
          self.pay = self.pay * (1 + pay_persent) + 500
      else:
          self.pay = self.pay * (1 + pay_persent) + 1000
          
if __name__=="__main__":
    LiSi=Manager('李四',12000,"初级")
    print(LiSi.get_last_name())
    LiSi.pay_raise(0.3)
    print(round(LiSi.pay))
    WangWu=Manager('王五',15000,"高级")
    print(WangWu.get_last_name())

    WangWu.pay_raise(0.2)
    print(round(WangWu.pay))