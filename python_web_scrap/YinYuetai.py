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

"""
请求的时候，需要用到的请求头的集合
"""
UserAgents = [
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
  "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
  "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
  "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
  "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

"""
请求的时候，需要用到的代理IP的集合
"""
PROXIES = [
'58.20.238.103:9797',
'123.7.115.141:9797',
'121.12.149.18:2226',
'176.31.96.198:3128',
'61.129.129.72:8080',
'115.238.228.9:8080',
'124.232.148.3:3128',
'124.88.67.19:80',
'60.251.63.159:8080',
'118.180.15.152:8102'    
]


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

#随机选取proxy代理
def getRandomProxy():  
    return random.choice(PROXIES)

#随机选取User_Agent
def getRandomHeaders():  
    return random.choice(UserAgents)

# 获取页面的Text数据
def getHTMLText(url):
    # header = getRandomHeaders()
    # proxy = getRandomProxy()
    try:
        # r = requests.get(url, headers=header, timeout=30, proxies=proxy)
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getMvsList(area, urls):
    # print urls
    url = 'http://vchart.yinyuetai.com/vchart/trends?area=ML&page=1';
    # for url in urls:
    #     pass
    html = getHTMLText(url)
    # print html
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
            item.releaseTime = tag.find('p', attrs={'class':'c9'}).get_text()
            items.append(item)
        
    except Exception as e:
        raise e
    # print len(items)
    handleMvsData(area, items)

def handleMvsData(area, items):
    areasDic = {'ML':'Mainland','HT':'Hongkong&Taiwan','US':'Americ','KR':'Korea','JP':'Japan'}
    fileName = "/Users/miraclewong/github/MoocStudy/python_web_scrap/YinYueTaiMvsList.txt"
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open(fileName, 'a') as f:
        f.write('%s -------%s\r\n' %(areasDic.get(area), nowTime))
        for item in items:
            f.write('%s %s \t %s \t %s \t %s \r\n' %(item.topNum, item.score, item.releaseTime, item.singer, item.mvName))
        f.write('\r\n'*4)




def main():
    urls = getURL()
    # items = getMvsList(urls)

if __name__ == '__main__':
    main()
