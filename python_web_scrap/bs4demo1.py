#!/anaconda3/bin/python
#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())