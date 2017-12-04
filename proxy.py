# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:39:39 2017

@author: juzheng
"""

import urllib.request
import re

def proxy_crawl(page):
    url = 'http://www.xicidaili.com/nn/' + str(page)
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen(url).read().decode('utf-8')
    html = str(html)
    pattern_IP = r'<td>(\d*?\.\d*?\.\d*?\.\d*?)</td>'
    pattern_dk = r'<td>(\d*?)</td>'
    IPlist = re.findall(pattern_IP, html)
    dklist = re.findall(pattern_dk, html)
    proxylist = []
    for i in range(0, 99):
        proxy_addr = str(IPlist[i]) + ':' + str(dklist[i])
        proxylist.append(proxy_addr)
    return proxylist

