#!/usr/bin/python
#-*- coding:utf8 -*-

import requests
import re
from bs4 import BeautifulSoup
import time

# client = pymongo.MongoClient('localhost', 27017)
# douban = client['douban']
# musictop = douban['musictop']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]

def get_url_music(url):
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html,'html.parser')
    music_hrefs = soup.select('a.nbg')
    for music_href in music_hrefs:
        get_music_info(music_href['href'])
        time.sleep(2)

def get_music_info(url):
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html,'html.parser')
    # names = soup.select('h1 > span')
    # authors = soup.select('span.pl > a')
    # styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />',wb_data.text,re.S)
    # times = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?)<br />',wb_data.text,re.S


def main():
    for url in urls:
        get_url_music(url)


if __name__ == '__main__':
    main()