# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:54:06 2017

@author: juzheng
"""

import urllib.request
import json

def dbcraw(i):
    pagevalue = (i - 1) * 20
    proxy = urllib.request.ProxyHandler({'http': '118.114.77.47:8080'})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    url = 'https://api.douban.com/v2/book/search?tag=%E7%BB%8F%E6%B5%8E%E5%AD%A6&start=' + \
        str(pagevalue) + '&fields='
    html = urllib.request.urlopen(url, timeout=100).read().decode('utf-8')
    content = json.loads(html)
    print(content)
    with open('D:\\简介.json', 'a') as fp:
        fp.writelines(json.dumps(content))
        fp.write('\n')
for i in range(1, 99):
    dbcraw(i)
