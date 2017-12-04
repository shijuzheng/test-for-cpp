# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:36:37 2017

@author: juzheng
"""

# C:/Users/juzheng/Desktop/cpp/词典/程度级别词语.txt
from collections import defaultdict

with open('C:\\Users\\juzheng\\Desktop\\cpp\\情感词典(评分)\\BosonNLP_sentiment_score\\BosonNLP_sentiment_score.txt', 'r', encoding='utf-8') as fp:
    NLPlist = fp.readlines()
with open('C:\\Users\\juzheng\\Desktop\\cpp\\词典\\负面评价词语.txt', 'r') as fp:
    No = fp.readlines()
Nolist = []
for line in No:
    Nolist.append(line.strip())
del Nolist[0]
del Nolist[0]
NLPdict = defaultdict()
wrong = []
for line in NLPlist:
    m = line.strip().split(' ')
    m = list(m)
    if len(m) == 2:
        NLPdict[m[0]] = m[1]
    else:
        wrong.append(m)
with open('C:\\Users\\juzheng\\Desktop\\cpp\\词典\\程度级别词语.txt', 'r') as fp:
    degree = fp.readlines()
degreelist = []
for line in degree:
    degreelist.append(line.strip())
mostlist = degreelist[3:72]
overlist = degreelist[202:232]
verylist = degreelist[74:116]
morelist = degreelist[118:155]
ishlist = degreelist[157:186]
insulist = degreelist[188:200]
Degreedict = defaultdict()
for word in mostlist:
    Degreedict[word] = 2
for word in overlist:
    Degreedict[word] = 1.75
for word in verylist:
    Degreedict[word] = 1.5
for word in morelist:
    Degreedict[word] = 1.25
for word in ishlist:
    Degreedict[word] = 1
for word in insulist:
    Degreedict[word] = 0.75
