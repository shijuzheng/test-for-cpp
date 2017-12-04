# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:32:29 2017

@author: juzheng
"""

import matplotlib.pyplot as plt
import pandas as pd

op = pd.read_csv('D:\\part_rate5.csv')
plt.figure()
x = op['rating']
plt.hist(x, bins=5)
plt.xlabel('rating')
plt.ylabel('qutity')
plt.title('frequency distribution histogram')
plt.savefig('C:\\Users\\juzheng\\Desktop\\cpp\\hist(rating).jpg')
plt.show()
