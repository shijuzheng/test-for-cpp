# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:50:47 2017

@author: juzheng
"""
import json
from pandas import DataFrame
import pandas as pd
from pricelist import pricefin
booklist = []
for eachline in open('D:\\text.json', 'r', encoding='utf-8'):
    r = json.loads(eachline)
    booklist.append(r['books'])
Numrater_list = []
averagerate_list = []
price_list = []
title_list = []
idlist = []
authorlist = []
wholelist = []
for booklist_list in booklist:
    for booklist_list_list in booklist_list:
        Numraters = booklist_list_list['rating']['numRaters']
        averagerate = booklist_list_list['rating']['average']
        price = booklist_list_list['price']
        title = booklist_list_list['title']
        bookid = booklist_list_list['id']
        author = booklist_list_list['author']
        Numrater_list.append(Numraters)
        averagerate_list.append(averagerate)
        price_list.append(price)
        title_list.append(title)
        idlist.append(bookid)
        authorlist.append(author)
data2 = {'author': authorlist,
         'rating': averagerate_list,
         'price': pricefin,
         'title': title_list,
         'ratenum': Numrater_list,
         'idlist': idlist
         }
frame2 = DataFrame(data2)
frame2.drop_duplicates('idlist', keep='first', inplace=True)
frame2.to_csv('D:\\booksfinal(noindex)bian.csv', encoding='utf-8')
frame2.to_csv('D:\\booksfinal(noindex).csv')
op = pd.read_csv('D:\\booksfinal(noindex)bian.csv')
price = op.ix[:, 'price']
print(type(price))
for i in range(len(price)):
    if price[i] == '':
        price[i] = 'None'
del op['price']
op['price'] = price
op.fillna(50.846701, inplace=True)
op.to_csv('D:\\booksfinal(noindex)bian.csv', encoding='utf-8')
op.to_csv('D:\\booksfinal(noindex).csv')
data = pd.read_csv('D:\\books(index=id)bian.csv')
col_ratenum = data.ix[:, 'ratenum']
s = col_ratenum.describe()
print(s)
col_rating = data.ix[:, 'rating']
k = col_rating.describe()
print(k)
col_price = data.ix[:, 'price']
l = col_price.describe()
print(l)
