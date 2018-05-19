#!/anaconda3/bin/python
#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re
soup = BeautifulSoup(
    open('/Users/miraclewong/github/MoocStudy/python_web_scrap/demo1.html'),
    'html.parser')
# print(soup.prettify())
print(soup.find_all(['a', 'b']))
for link in soup.find_all(['a', 'b']):
    print(link.get('href'))

print(soup.find_all('p', 'course'))
print(soup.find_all(id='link1'))
print(soup.find_all(id='link'))
print(soup.find_all(id=re.compile('link')))