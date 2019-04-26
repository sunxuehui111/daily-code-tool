import yaml
import shutil
import os
import time
import logging
import datetime
import re
'''
步骤：
1.进入年文件夹
2.判断月份--一个月之前的文件夹
3.进入月文件夹--判断日文件夹--当前日一个月以前
4.进入日文件夹--固定，时间大于005959 可切片 删除7z文件

1.进入年文件夹
2.判断月份--三个月之前的文件夹
3进入月文件夹--判断日文件夹--是否当月周一--不是则删除文件夹

固定路径://backup
年-0000
月-00
日-00
7z文件 mwo.年月日小时分钟秒
mwo.0000 00 00 00 00 00
例如： mwo.2019 04 19 14 49 03
'''

class Writelog(object):
	"""docstring for writelog"""
	logger = logging.getLogger(__name__)
	logger.setLevel(level = logging.INFO)
	handler = logging.FileHandler("delete_log.txt")
	handler.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)


class ClearBackupFile(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.wlog = Writelog 
		self.yearName = ''
		self.monthName = ""
		self.dayName = ''
		self.dateName = ""
		self.get_daylist = []
	#获取当前时间并对时间进行处理,返回年，月，日
	def getTime(self):
		self.dateName = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		self.wlog.logger.info("当前时间为:" + self.dateName)
		self.yearName = time.strftime('%Y',time.localtime(time.time()))
		self.monthName = time.strftime('%m',time.localtime(time.time()))
		self.dayName = time.strftime('%d',time.localtime(time.time()))

	#遍历指定路径下的月文件夹
	def traverseMonthDir(self,path,monthNum):
		Dirpath = path + "//" +  self.yearName
		fs = os.listdir(Dirpath)
		dirPath = []
		for f in fs:
			temp_path = os.path.join(Dirpath,f)
			if os.path.isdir(temp_path):
				if (int(self.monthName) - monthNum) > int(f):
					temp_path = Dirpath + "//" + f
					dirPath.append(temp_path)
		wlog.logger.info("获得要删除%d个月之前的的文件目录列表" % monthNum)
		return dirPath

	#遍历月目录下的日目录
	def traverseDayDir(self,monthDirPath,weeknum):
		dirPath = []
		for Dirpath in monthDirPath:
			fs = os.listdir(Dirpath)
			for f in fs:
				temp_path = os.path.join(Dirpath,f)
				if os.path.isdir(temp_path):				
					dirpath_time = re.sub("\D", "", temp_path) 
					dirpath_time = datetime.datetime.strptime(dirpath_time, "%Y%m%d").strftime("%w")
					if dirpath_time != weeknum:
						getdaydir =  Dirpath + "//" + f
						self.get_daylist.append(getdaydir)
					temp_path = Dirpath + "//" + f
					dirPath.append(temp_path)
		wlog.logger.info("获得保留的星期%d目录列表" % weeknum)
		return dirPath

	#遍历日目录下的文件
	def traverseFile(self,filePathList):
		filepath = []
		for filePath in filePathList:
			fs = os.listdir(filePath)
			for f in fs:
				temp_path = os.path.join(filePath,f)
				if not os.path.isdir(temp_path):
					temp_path_name = f[-9:-3]
					if int(temp_path_name) > int("005959"):
						temp_path = filePath + "//" + f
						filepath.append(temp_path)
		wlog.logger.info("获得要删除的文件列表")
		return filepath

	#删除文件
	def del_file(self,file_path_list):   
   		for path_file in  file_path_list:
   			if os.path.isfile(path_file):     #判断是否是文件
   				os.remove(path_file)
   				wlog.logger.warning("已删除文件：" + path_file)
   			else:
   				wlog.logger.warning("删除文件失败" + path_file + "不是文件!")
#删除文件夹            
	def del_dir(self):
		for path_dir in self.get_daylist:
			if os.path.isdir(path_dir):#判断是否是目录
				shutil.rmtree(path_dir,True)
				wlog.logger.warning("已删除目录：" + path_dir)
			else:
				wlog.logger.warning("删除目录失败" + path_file + "不是文件夹!")

if __name__ == "__main__":
	wlog = Writelog()
	clear_object = ClearBackupFile()
	# 获取当前脚本所在文件夹路径
	curPath = os.path.dirname(os.path.realpath(__file__))
	# 获取yaml文件路径
	yamlPath = os.path.join(curPath, "deleteDateFile.yaml")
 
	# open方法打开直接读出来
	f = open(yamlPath, 'r', encoding='utf-8')
	cfg = f.read()
	yamldic = yaml.load(cfg)
	path = yamldic['rootDir']
	month_num = yamldic['monthNum']
	weekday_num = yamldic['weekdayNum']
	wlog.logger.info("读取配置成功")
	wlog.logger.info("开始删除任务")
	clear_object.getTime()
	wlog.logger.info("获取日期信息成功")
	try:
		dir_mon = clear_object.traverseMonthDir(path,month_num)
		dir_day = clear_object.traverseDayDir(dir_mon,weekday_num)
		file_list = clear_object.traverseFile(dir_day)
	except Exception as e:
		wlog.logger.error("文件路径处理失败,错误信息为:%s" % e)
	else:
		wlog.logger.info("文件路径处理成功!!!")
	try:
		#删除文件
		clear_object.del_file(file_list)
		#删除目录
		clear_object.del_dir()
	except Exception as e:
		wlog.logger.error("删除文件失败！,错误信息为:%s" % e)
	else:
		wlog.logger.info("操作完成！无任何错误信息！")
