#!/usr/bin/python
#-*- coding:utf8 -*-

"""
本程序用来获取音乐台网站的NV排行榜的数据
音悦台：http://www.yinyuetai.com

参考书籍
《用Python写网络爬虫》
《Python网络爬虫实战》
"""
import requests
import sys
import os
import re
import random
import time
from bs4 import BeautifulSoup

reload(sys)  
sys.setdefaultencoding('utf8')
"""
Item 代表一个MV榜单
"""
class Item(object):
    topNum = None  #排名
    score = None  #打分 desc_score:趋势下降 asc_score：趋势上升
    mvName = None  #MV名字
    singer = None  #演唱者
    releasTime = None  #释放时间

'''获取url地址
初始化整个程序的数据，包含网址，以及需要用到的字典和列表等'''
def getURL():
    urlBase = 'http://vchart.yinyuetai.com/vchart/trends?'
    areas = ['ML','HT','US','KR','JP']  # 和后面的areaDict相对应
    pages = [str(i) for i in range(1,4)]
    urls = []
    for area in areas:
        for page in pages:
            urlEnd = 'area=' + area + '&page=' + page
            url = urlBase + urlEnd
            urls.append(url)
        getMvsList(area, urls)
    # return urls

# 获取页面的Text数据
def getHTMLText(url):
    try:
        # r = requests.get(url, headers=header, timeout=30, proxies=proxy)
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 获取页面上的专辑的数据
def getMvsList(area, urls):
    url = 'http://vchart.yinyuetai.com/vchart/trends?area=ML&page=1';
    html = getHTMLText(url)
    items = []
    try:
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('li', attrs={'name':'dmvLi'})
        for tag in tags:
            item = Item()
            item.topNum = tag.find('div', attrs={'class':'top_num'}).get_text()
            if tag.find('h3', attrs={'class':'desc_score'}):
                item.score = tag.find('h3', attrs={'class':'desc_score'}).get_text()
            else:
                item.score = tag.find('h3', attrs={'class':'asc_score'}).get_text()
           
            item.mvName = tag.find('img').get('alt')
            item.singer = tag.find('a', attrs={'class':'special'}).get_text()
            pst = re.compile(r'\d{4}-\d{2}-\d{2}')
            item.releaseTime = pst.findall(tag.find('p', attrs={'class':'c9'}).get_text())[0]
            items.append(item)
        
    except Exception as e:
        raise e
    handleMvsData(area, items)

def handleMvsData(area, items):
    areasDic = {'ML':'Mainland','HT':'Hongkong&Taiwan','US':'Americ','KR':'Korea','JP':'Japan'}
    fileName = "/Users/miraclewong/github/MoocStudy/python_web_scrap/YinYueTaiMvsList.txt"
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    tplt = "{:8}\t{:10}\t{:20}\t{:20}\t{:16}\r\n"
    with open(fileName, 'a') as f:
        f.write('%s -------%s\r\n' %(areasDic.get(area), nowTime))
        f.write(tplt.format("排名","得分","发布时间","歌手","专辑名称"))
        for item in items:
            f.write('%s \t %s \t %s \t %s \t\t %s \r\n' %(item.topNum, item.score, item.releaseTime, item.singer, item.mvName))
        f.write('\r\n'*4)




def main():
    urls = getURL()
    # items = getMvsList(urls)

if __name__ == '__main__':
    main()
