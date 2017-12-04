# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:03:27 2017

@author: juzheng
"""

import jieba
from collections import defaultdict

with open('D:\\intro.txt', 'r', encoding='utf-8') as file:
    s = file.read()
stopwordlist = []
with open('C:/Users/juzheng/Desktop/tyc.txt', 'r') as file:
    line = file.readlines()
    for stopword in line:
        stopwordlist.append(stopword.strip())
seg_list = jieba.cut(s, cut_all=False)
wordlist = []
for word in seg_list:
    if word not in stopwordlist:
        wordlist.append(word)
words = defaultdict()
for word in wordlist:
    if word not in words.keys():
        words[word] = 1
    if word in words.keys():
        words[word] += 1
del words[' ']
del words['\n']
del words['p']
del words['intro']
del words['class']
del words['div']
key = words.keys()
value = words.values()
key = list(key)
value = list(value)
l = defaultdict()
for i in range(len(words)):
    l[value[i]] = key[i]
num = l.keys()
name = l.values()
num = list(num)
name = list(name)
num.sort(reverse=True)
f = defaultdict()
for i in range(len(num)):
    f[num[i]] = l[num[i]]
print(f)
