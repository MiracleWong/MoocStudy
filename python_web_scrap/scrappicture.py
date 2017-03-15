#!/usr/bin/python
#-*- coding:utf8 -*-

import requests
import os


url = "http://image.nationalgeographic.com.cn/2017/0309/20170309045245498.jpg"
root = "/Users/miraclewong/github/MoocStudy/Pictures/"

path = root + url.split('/')[-1]
# path = url.split('/')[-1]
print path
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件保存失败")
except Exception as e:
	print e
	print("爬取失败")
