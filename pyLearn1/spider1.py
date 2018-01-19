"""from urllib import request  
from  bs4 import BeautifulSoup  
import re  
import time  
  
url = "https://www.zhihu.com/question/22918070"  
html = request.urlopen(url).read().decode('utf-8')  
soup = BeautifulSoup(html,'html.parser')  
#print(soup.prettify())  
  
#用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句  
links = soup.find_all('img', "origin_image zh-lightbox-thumb",src=re.compile(r'.jpg$'))  
print(links)  
  
# 设置保存图片的路径，否则会保存到程序当前路径  
path = r'images'                            #路径前的r是保持字符串原始值的意思，就是说不对其中的符号进行转义  
for link in links:  
    print(link.attrs['src'])  
    #保存链接并命名，time.time()返回当前时间戳防止命名冲突  
    request.urlretrieve(link.attrs['src'],path+'\%s.jpg' % time.time())  #使用request.urlretrieve直接将所有远程链接数据下载到本地  
"""
"""
import urllib.request
url = 'http://www.wangxindhj.xin'
page_info = urllib.request.urlopen(url).read()
page_info = page_info.decode('gbk')
print(page_info)

url = 'http://www.baidu.com'
# page = request.Request(url)
# page.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = urllib.request.Request(url, headers=headers)
page_info = urllib.request.urlopen(page).read().decode('utf-8')
print(page_info)
"""

#beautifull soup#
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup,element
soup = BeautifulSoup(html_doc,'lxml')
"""print(soup.prettify())
print(soup.title,soup.title.name,soup.title.string,sep = '\n')
print(soup.title.parent.name,soup.p,soup.p['class'],sep = '\n')
print(soup.find_all('a'),soup.find(id = 'link3'),sep = '\n')
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.text)"""
def circlefind(soup,n):
    n += 1
    for child in soup.children:
        print("*"*n,child,sep = '\n')
        if(type(child) != element.NavigableString):
            circlefind(child,n)
#circlefind(soup,0)
"""
Tag = soup.a   
print(Tag,Tag.name,Tag['class'],Tag.attrs)
print(type(Tag.string))
print(soup.body.contents)
print(soup.contents)
print(soup.name,soup.contents[0].name)
#子孙
for child in soup.descendants:
    print(child)
print(len(list(soup.children)),len(list(soup.descendants)))
"""
for string in soup.strings:
    print(repr(string))
for string in soup.stripped_strings:
    print(repr(string))