from urllib import request
from bs4 import BeautifulSoup
import re
import time
"""
html_url = 'http://www.chinadaily.com.cn'
html_contents = request.urlopen(html_url).read().decode('utf-8')
beautifull = BeautifulSoup(html_contents,'lxml')
test2 = beautifull.find_all('a')
LUrl = []
for te in test2:
    s = te.get('href')
    if re.search(r'^http://www.chinadaily.com.cn',s):
        LUrl.append(s)
        print(s)
set1 = set(LUrl)
LUrl = list(set1)
LUrl.sort()
maxlen = len(LUrl)
idex = 0
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
for i in LUrl:
    print('%d : %d' % (maxlen,idex))
    req = request.Request(url=i, headers=headers)
    try:
        html = request.urlopen(req,timeout = 8)
    except:
        print('异常：',html.getcode())
        continue
    try:
        html_contents = html.read().decode('utf-8')
    except:
        try:
            html_contents = html.read().decode('gbk')
            print('gbk！')
        except:
            continue
    beautifull = BeautifulSoup(html_contents,'lxml')
    test2 = beautifull.find_all('a')
    for te in test2:
        s = te.get('href')
        if s != None:
            if re.search(r'^http://www.chinadaily.com.cn',s):
                if re.search('.html$',s) and not s in LUrl:
                    LUrl.append(s)
    print(len(LUrl))
    if idex % 100 == 0:
        fp = open('urllist.txt','w')
        for i in LUrl:
            fp.write(i + '\n')
        fp.close()
    if len(LUrl) > 100000:
        break
    idex +=1    
fp = open('urllist.txt','w')
for i in LUrl:
    fp.write(i + '\n')
fp.close()
"""
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
fp = open('urllist.txt')
LUrl = fp.read().split()
fp.close()
fp = open('context.txt','w',encoding = 'utf-8')
idex = 0
for i in LUrl:
    s1 = ''
    print(idex)
    idex +=1
    req = request.Request(url=i, headers=headers)
    try:
        html = request.urlopen(req,timeout = 10)
    except:
        continue
    try:
        html_contents = html.read().decode('utf-8')
    except:
        continue
    beautifull = BeautifulSoup(html_contents,'lxml')
    text = beautifull.find_all('p')
    for j in text:
        if j.string !=None:
            s1 = s1 + j.string
    fp.write(s1)
fp.close()