#!/anaconda3/bin/python
#-*- coding: UTF-8 -*-
import requests


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:100]
    except:
        return "生产异常"


def main():
    # url = "https://item.jd.com/27462769971.html"
    url = "https://www.amazon.cn/dp/B00C4OM7V0/ref=pd_sim_14_3?_encoding=UTF8&psc=1&refRID=H1EVRXNA58PXXVXN3QTS"
    print(getHTMLText(url))


if __name__ == '__main__':
    main()
