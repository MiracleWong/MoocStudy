#!/usr/bin/python
#-*- coding:utf8 -*-

import pandas as pd

b = pd.Series([9,8,7,6],index=['a','b','c','d'])
s = pd.Series(25,index=['a','b','c'])
d = pd.Series({'a':9, 'b':8, 'c':7})
e = pd.Series({'a':9, 'b':8, 'c':7}, index=['c', 'a', 'b','d'])
print b 
a = s + d
print a