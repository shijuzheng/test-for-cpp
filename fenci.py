# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:16:21 2017

@author: juzheng
"""

import jieba
with open('C:/Users/juzheng/Desktop/12.txt', 'r') as fp:
    s = fp.read()
seg_list = jieba.cut(s, cut_all=False)
jieba.suggest_freq('学经济', True)
stopwordlist = []
with open('C:/Users/juzheng/Desktop/tyc.txt', 'r') as file:
    line = file.readlines()
    for stopword in line:
        stopwordlist.append(stopword.strip())
i = 0
wordlist = []
for word in seg_list:
    if word not in stopwordlist:
        if word != '\n':
            wordlist.append(word)
print(wordlist)
