# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:08:30 2017

@author: juzheng
"""


from 代理 import proxy_crawl              #返回一个代理列表，参数为n,代理数量为n*100
import urllib.request
import http.cookiejar
import re
import time
from pandas import DataFrame
import pandas as pd

proxylist=proxy_crawl(20)
p=10
proxy_addr=proxylist[p]
noprice=[]
baseurl='https://book.douban.com/subject/'
headers={"Host": "book.douban.com",
"Connection":"keep-alive",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8",
"Referer":"https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6"
}
headerall=[]
for (key,value) in headers.items():
    item=(key,value)
    headerall.append(item)

op=pd.read_csv('D:\\booksfinal(noindex)bian.csv')
opid=op['idlist']
IDlist=list(opid)

whole={}
def price_crawl(idnum,proxy_addr):
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    cjar=http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler(),urllib.request.HTTPCookieProcessor(cjar))
    opener.addheaders=headerall
    urllib.request.install_opener(opener)
    url=baseurl+str(idnum)+'/'
    html=urllib.request.urlopen(url).read().decode('utf-8')
    html=str(html)
    pattern1='<span class="">在哪儿买这本书</span>(.+?)<div class="add2cartContainer ft no-border">'
    pricepart=re.findall(pattern1,html,re.S) 
    if pricepart==[]:
        pattern2='<span class="">其他版本有售</span>(.+?)<div class="add2cartContainer ft no-border">'
        pricepart=re.findall(pattern2,html,re.S)
        if pricepart!=[]:
            pricepart=pricepart[0]
            
            web_pattern=r'<a target="_blank" href=".+?">\s+?(\w+?)\s+?</a>'
            price_pattern=r'<a class="buylink-price" target="_blank" href=".+?">\s+?<span class="">\s+?(\d+?\.\d+?) 元</span>'
            web=re.findall(web_pattern,pricepart)
            price=re.findall(price_pattern,pricepart)
            for i in range(len(web)):
                wp[web[i]]=str(price[i])
            whole[idnum]=wp
        else:
            print('no other price')
            print(str(idnum))
            noprice.append(idnum)
    else:
        pricepart=pricepart[0]
        web_pattern=r'<a target="_blank" href=".+?" class="">\s+?<span class="">(.+?)</span>'
        price_pattern=r'<a target="_blank" href=".+?" class="buylink-price ">\s+?<span class="">\s+?(\d+?\.\d+?) 元\s+?</span>'
        web=re.findall(web_pattern,pricepart)
        price=re.findall(price_pattern,pricepart)            
        for i in range(len(web)):
            wp[web[i]]=str(price[i])
            whole[idnum]=wp
        
    time.sleep(5)
   
for i in range(len(IDlist)):
    wp={}
    try:
        price_crawl(IDlist[i],proxy_addr)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e)
        if hasattr(e,"reason"):
            print(e)
        p+=1
        proxy_addr=proxylist[p]


        
idlist=whole.keys()
pricelist=whole.values()
idlist=list(idlist)
pricelist=list(pricelist)
frame=DataFrame({'id':idlist,
                'otherprice':pricelist
                 })
frame.to_csv('D:\\otherprice.csv')
    

        
    

    
    
