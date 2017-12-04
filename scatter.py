# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:11:18 2017

@author: juzheng
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

op = pd.read_csv('D:\\part_num5000&rate5.csv')
xlist = op['ratenum']
ylist = op['rating']
def xy(xlist, ylist):  # 计算一元线性回归方程中的参数
    n = len(list(xlist))
    x = np.array(xlist)
    y = np.array(ylist)
    sumx = x.sum()
    sumy = y.sum()
    xy = np.multiply(x, y)
    sumxy = xy.sum()
    x2 = np.square(x)
    sumx2 = x2.sum()
    sum2x = np.square(sumx)
    beita1 = (n * sumxy - sumx * sumy) / ((n * sumx2) - sum2x)
    avx = x.mean()
    avy = y.mean()
    beita0 = avy - beita1 * avx
    return beita1, beita0
beita1, beita0 = xy(xlist, ylist)
plt.figure()
x = xlist
y = beita1 * x + beita0
plt.plot(x, y)
plt.scatter(xlist, ylist)
plt.xlabel('ratenum')
plt.ylabel('rating')
plt.title('simple linear regression')
# plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
# plt.xticks([5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])
plt.savefig('C:\\Users\\juzheng\\Desktop\\cpp\\numandrate.jpg')
plt.show()
