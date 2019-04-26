# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:32:58 2019

@author: ctrpg
"""

'''from PIL import Image
im = Image.open('C:/Users/ctrpg/Desktop/test/猴子/frame_00017.png')#返回一个Image对象
print('宽：%d,高：%d'%(im.width,im.height))'''



'''from PIL import Image
import numpy as np

image=Image.open('C:/Users/ctrpg/Desktop/photoCut/frame_00001.png')
image.load()

image_data = np.asarray(image)
image_data_bw = image_data.max(axis=2)
non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]

new_image = Image.fromarray(image_data_new)
new_image.save('C:/Users/ctrpg/Desktop/photoCut/frame_00001new.png')'''


'''import os
from PIL import Image
import numpy as np
path = r"C:/Users/ctrpg/Desktop/photoCut/"
for filename in os.listdir(path): 
    image=Image.open(path + filename)
    image.load()
    image_data = np.asarray(image)
    image_data_bw = image_data.max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
    image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]
    new_image = Image.fromarray(image_data_new)
    new_image.save(r"C:/Users/ctrpg/Desktop/newPhoto/" + filename)'''
    
    
#单个文件夹 裁剪
import yaml
import os
from PIL import Image
import numpy as np

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "photoPath.yaml")
 
# open方法打开直接读出来
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()
yamldic = yaml.load(cfg)  # 用load方法转字典
rootpath = yamldic['rootPath']
targetpath = yamldic['targetPath']
listPngpath = []
path_list=os.listdir(rootpath)
print('--开始执行程序--')
for filename in path_list:
    if os.path.splitext(filename)[1] == '.png':
        listPngpath.append(filename)
if len(listPngpath) == 0:
    print("文件夹中为空！！！")
image=Image.open(rootpath + listPngpath[0])
image.load()
image_data = np.asarray(image)
image_data_bw = image_data.max(axis=2)
non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
count = 1
countrows = len(non_empty_rows)
countcolumns = len(non_empty_columns)

while 1:
    if countrows % 4 != 0:
        countrows += 1
    if countcolumns % 4 != 0:
        countcolumns += 1
    count += 1
    if countrows % 4 == 0 and countcolumns % 4 == 0:
        break
cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
 
image_data_new = image_data[cropBox[0]:cropBox[1] + count, cropBox[2]:cropBox[3] + count , :]
new_image = Image.fromarray(image_data_new)
new_image.save(targetpath + listPngpath[0])
print('裁剪<%s>,完成！'%listPngpath[0])
for pngname in listPngpath[1::]:
    png=Image.open(rootpath + pngname)
    png.load()
    png_data = np.asarray(png)
    png_data_new = png_data[cropBox[0]:cropBox[1] + count, cropBox[2]:cropBox[3]  + count, :]
    new_png = Image.fromarray(png_data_new)
    new_png.save(targetpath + pngname)
    print('裁剪<%s>,完成！'% pngname)
print('--程序执行完毕--')
os.system("pause")