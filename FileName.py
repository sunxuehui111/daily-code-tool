# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:15:41 2019

@author: ctrpg
"""
import os
import shutil
import re
import yaml

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "photoNamePath.yaml")
 
# open方法打开直接读出来
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()
yamldic = yaml.load(cfg)  # 用load方法转字典

path = yamldic['dicpath']
n = yamldic['direction']
#新建n个方向文件夹
sort_folder_number = [x for x in range(0,n)]
for number in sort_folder_number:
    new_folder_path = os.path.join(path,'%s'%number)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

#列出文档
file_list = os.listdir(path)
#提取出文档名称内的数字，并根据数字决定将文件发往那个文件夹
for i in range(len(file_list)):
    old_file_path = os.path.join(path,file_list[i])
    if os.path.isdir(old_file_path):
        pass
    elif not os.path.exists(old_file_path):
        pass
    else:
        file_name_number = re.findall(r'\d+',file_list[i])[0]
        file_name_number = int(file_name_number)
        new_file_path = os.path.join(path,'%s'%(file_name_number%8))
        shutil.move(old_file_path,new_file_path)
