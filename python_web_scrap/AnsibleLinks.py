#!/usr/bin/python
#-*- coding:utf-8 -*-

#CrawUnivRankingA.py
import sys
import requests
from bs4 import BeautifulSoup
import re

reload(sys)
sys.setdefaultencoding( "utf-8" )

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getLinksList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all('a',attrs={'target':'_blank'})
    for i in a:
        try:
            print i
            href = i.attrs['href']
            # ulist.append(re.findall(r"Ansible ", href)[0])
        except Exception as e:
            raise e
    print ulist
def printLinksList(printUnivList,num):
    print("{:^16}\t{:^20}".format("文章名称","文章链接"))
    for i in range(num):
        u=ulist[i]
        print("{:^16}\t{:^20}".format(u[0],u[1]))

def main():
    uinfo = []
    # url = 'http://www.jianshu.com/p/667dabe96f04'
    url = 'http://www.jianshu.com/p/8b17779febf3'
    html = getHTMLText(url)
    getLinksList(uinfo, html)
    # printLinksList(uinfo,20)
    # printUnivList(uinfo, 100) # 20 univs
main()
