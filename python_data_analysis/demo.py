#!/usr/bin/python
#-*- coding:utf8 -*-

import matplotlib.pyplot as plt

plt.plot([3, 1, 4, 5, 2])
plt.ylabel("Grade")
plt.savefig('test', dpi=600)
plt.show()
