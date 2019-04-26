import os
import requests
from lxml import etree



class Spider(object):
	"""docstring for Spider"""
	def get_novelName(self):
	#获取小说名 创建文件夹
		reponse = requests.get("https://www.qidian.com/all")
		xml = etree.HTML(reponse.text)
		Big_title_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/text()')
		Big_src_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/@href')
		print("--链接到小说网--")
		for bigtitle,bigsrc in zip(Big_title_list,Big_src_list):
			if os.path.exists(bigtitle) == False:
				os.mkdir(bigtitle)
			self.get_novelCatg(bigtitle,bigsrc)
	def get_novelCatg(self,bigtitle,bigsrc):
	#获取章节目录
		reponse = requests.get("http:" + bigsrc)
		xml = etree.HTML(reponse.text)
		Little_title_list = xml.xpath('//ul[@class="cf"]/li/a/text()')
		Little_src_list = xml.xpath('//ul[@class="cf"]/li/a/@href')
		for littletitle,littlesrc in zip(Little_title_list,Little_src_list):
			self.save_novel(bigtitle,littletitle,littlesrc)
	def save_novel(self,bigtitle,littitle,litsrc):
	#保存小说
		reponse = requests.get("http:" + litsrc)
		xml = etree.HTML(reponse.text)
		contents = "\n".join(xml.xpath('//div[@class="read-content j_readContent"]/p/text()'))
		fileName = bigtitle + "\\" + littitle + ".txt"
		print("--正在存储小说<" + littitle + ">--")
		with open(fileName,"w",encoding='utf-8') as f:
			f.write(contents)
spider = Spider()
spider.get_novelCatg("凡人修仙之仙界篇","//book.qidian.com/info/1010734492")
#spider.get_novelName()