#!/usr/bin/python
#-*- coding:utf8 -*-

from bs4 import BeautifulSoup
import requests
import sys
import os
import re
import time
import resource
import random
import random


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

# get the text of HTML Page
def getHTMLText(url):
    '''从页面返回数据 '''
    fakeHeaders = {'User-Agent':getRandomHeaders()}
    try:
        r = requests.get(url, headers=headers, timeout=30, proxies = getRandomProxy)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# Get the list of the Top250 Movies
def getMoviesList(moviesList, movieURL):
    html = getHTMLText(movieURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            moviesList.append(re.findall(r"\d{7,8}", href)[0])
        except:
            continue
    moviesList = list(set(moviesList))
    print len(moviesList)
    # print moviesList
    # return moviesList

def getMoviesInfo(moviesList, movieURL):
    count = 0
    for movieInfo in moviesList:
        url = movieURL + movieInfo + "/"
        html = getHTMLText(url)
    print len(url)


def getRandomProxy():  #随机选取proxy代理
    return random.choice(resource.PROXIES)
 
def getRandomHeaders():  #随机选取文件头
    return random.choice(resource.UserAgents)

proxies = { "http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080", }  

def main():
    
    movies_top250_urls = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    # movies_top250_url = 'https://movie.douban.com/top250'
    moives_info_url = 'https://movie.douban.com/subject/'
    moviesList = []
    for url in movies_top250_urls:
        getMoviesList(moviesList,url)
    # print len(moviesList)
    # getMoviesInfo(moviesList,moives_info_url)


if __name__ == '__main__':
    main()
