#!/anaconda3/bin/python
#-*- coding:utf8 -*-

from bs4 import BeautifulSoup
import requests
import sys
import os
import re
import traceback


def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        r.encoding = code
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        print url
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            name = stockInfo.find(attrs={'class': 'bets-name'})
            print type(name)
            # infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text.strip()
                value = valueList[i].text.strip()
                infoDict[key] = value
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()
            # continue


def getStockInfo(lst, stockURL):
    count = 0

    # url = stockURL + lst[278] + ".html"
    url = "https://gupiao.baidu.com/stock/sh166105.html"
    # print url
    html = getHTMLText(url)
    print html
    try:
        infoDict = {}
        # soup = BeautifulSoup(html, 'html.parser')
        # stockInfo = soup.find('div', attrs={'class':'stock-bets'})
        # name = stockInfo.find(attrs={'class':'bets-name'})
        # infoDict.update({'股票名称':name.text.split()[0]})
        # print infoDict['股票名称']
        # keyList = stockInfo.find_all('dt')
        # valueList = stockInfo.find_all('dd')
        # for i in range(len(keyList)):
        #     key = keyList[i].text.strip()
        #     value = valueList[i].text.strip()
        #     infoDict[key] = value
        #     print key + ":" + infoDict[key]
    except:
        traceback.print_exc()


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    stocksList = []
    output_file = "/Users/miraclewong/github/MoocStudy/python_web_scrap/BaiduStocks.txt"
    getStockList(stocksList, stock_list_url)
    getStockInfo(stocksList, stock_info_url)
    getStockInfo(stocksList, stock_info_url, output_file)


if __name__ == '__main__':
    main()
