#!/usr/bin/python
#-*- coding:utf8 -*-

import pandas as pd
import numpy as np
import sys
print sys.getdefaultencoding()
d = pd.DataFrame(np.arange(10).reshape(2,5))
print d
dl = {'one':[1, 2, 3, 4], 'two':[9, 8, 7, 6]}
d1 = pd.DataFrame(dl, index=['a','b','c','d'])
print d1

dl2 = {'城市':['北京', '上海', '广州', '深圳', '沈阳'],
        '环比':[101.5, 101.2, 101.3, 102.0, 100.1],
        '同比':[120.7, 127.3, 119.4, 140.9, 101.4],
        '定基':[121.4, 127.8, 120.0, 145.5, 101.6]}
d2 = pd.DataFrame(dl2, index=['c1','c2','c3','c4','c5'])
# print d2
nd = d2.reindex(columns=['城市','同比','环比', '定基'])
print nd
newc = nd.columns.insert(4,'新增')
newd = nd.reindex(columns=newc, fill_value=200)
print newd