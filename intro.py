# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:46:44 2017

@author: juzheng
"""

import urllib.request
import re
import pandas as pd
import http.cookiejar
from 代理 import proxy_crawl
import time

op = pd.read_csv('D:\\booksfinal(noindex)bian.csv')
opid = op['idlist']
idlist = list(opid)
print(type(idlist))
proxylist = proxy_crawl(9)
headers = {
    "Host": "book.douban.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Referer": "https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6"}
headerall = []
for (key, value) in headers.items():
    item = (key, value)
    headerall.append(item)
baseurl = 'https://book.douban.com/subject/'
p = 2
proxy_addr = proxylist[p]
def crawl(idnum, proxy_addr):
    url = baseurl + str(idlist[i]) + "/"
    cjar = http.cookiejar.CookieJar()
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(
        proxy,
        urllib.request.HTTPHandler(),
        urllib.request.HTTPCookieProcessor(cjar))
    opener.addheaders = headerall
    urllib.request.install_opener(opener)
    content = urllib.request.urlopen(url).read().decode('utf-8')
    content = str(content)
    pattern = r'<div class="intro">(.+?)</p>'
    intro = re.search(pattern, content, re.S).group(0)
    print(intro)
    with open('D:\\intro.txt', 'a', encoding='utf-8') as fp:
        fp.writelines(intro)
        fp.writelines('\n')
    time.sleep(5)
for i in range(len(idlist)):
    try:
        crawl(idlist[i], proxy_addr)
    except urllib.request.URLError as e:
        print(e)
        p = p + 1
        proxy_addr = proxylist[p]
    except BaseException:
        print(idlist[i])
