#!/usr/bin/python
#-*- coding:utf8 -*-

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=20

a = np.arange(0.0, 5.0, 0.02)
plt.xlabel('横轴: 时间')
plt.ylabel('纵轴: 正弦')
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()
