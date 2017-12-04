# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 01:15:05 2017

@author: juzheng
"""

import jieba
from collections import defaultdict
from DICT import Nolist, Degreedict, NLPdict
import os
import matplotlib.pyplot as plt

filelist = os.listdir('C:\\Users\\juzheng\\Desktop\\pinglun')
def fileopen(filename):
    with open(filename, 'r') as fp:
        chap = fp.read()
    with open('C:\\Users\\juzheng\\Desktop\\tyc.txt', 'r') as fp:
        stopwords = fp.readlines()
    stopwordlist = []
    for word in stopwords:
        stopwordlist.append(word.strip())
    wordlist = []
    words = jieba.cut(chap, cut_all=False)
    for word in words:
        if word not in stopwordlist:
            if word != ' ':
                wordlist.append(word)
    print(wordlist)
    worddict = defaultdict()
    i = 0
    for word in wordlist:
        worddict[word] = i
        i = i + 1
    NLP = NLPdict.keys()
    degree = Degreedict.keys()
    senword = defaultdict()
    degreeword = defaultdict()
    noword = defaultdict()
    NLPl = []
    degreel = []
    nol = []
    p = 0
    for word in wordlist:
        if word == '。':
            p = p + 1
        if word in NLP:
            if word not in degree:
                if word not in Nolist:
                    NLPl.append(word)
                    senword[worddict[word]] = NLPdict[word]
        if word in degree:
            if word not in Nolist:
                degreel.append(word)
                degreeword[worddict[word]] = Degreedict[word]
        if word in Nolist:
            nol.append(word)
            noword[worddict[word]] = -1
    senloc = senword.keys()
    degreeloc = degreeword.keys()
    noloc = noword.keys()
    senloc = list(senloc)
    degreeloc = list(degreeloc)
    noloc = list(noloc)
    sennum = -1
    Sum = 0
    for i in range(len(wordlist)):
        d = 1
        score = 0
        if i in senloc:
            score = d * float(senword[i])
            sennum += 1
        if sennum < len(senloc) - 1:
            for j in range(senloc[sennum - 1], senloc[sennum]):
                if j in noloc:
                    d *= -1
                elif j in degreeloc:
                    score = score * d * float(degreeword[j])
        Sum += score
    ave = Sum / p
    return ave
result = []
for file in filelist:
    filename = 'C:\\Users\\juzheng\\Desktop\\pinglun\\' + file
    m = fileopen(filename)
    result.append(m)
plt.figure()
x = [1, 2, 3, 4, 5]
y = result
plt.scatter(x, y)
plt.xticks([1, 2, 3, 4, 5])
plt.ylabel('score')
plt.savefig('C:\\Users\\juzheng\\Desktop\\score2.jpg')
plt.show()
