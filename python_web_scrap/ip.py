#!/usr/bin/python
#-*- coding:utf8 -*-

import requests
import os


url = "http://m.ip138.com/ip.asp?ip="
r = requests.get(url + "202.204.80.112")
print r.url
