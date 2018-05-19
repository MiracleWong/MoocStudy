# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


soup = BeautifulSoup(open('/Users/miraclewong/github/MoocStudy/python_web_scrap/demo.html'), 'html.parser')
tag = soup.a
print soup.a.parent.parent.name
print tag.attrs
print tag.attrs['class']
print tag.attrs['href']
print type(tag.attrs)
print type(tag)
print soup.a.string
print soup.p
print soup.p.string
print soup.p.get_text()