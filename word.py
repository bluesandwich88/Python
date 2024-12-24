#!/usr/bin/python
# coding=UTF-8
import requests
import urllib.request
# import urllib as UrlUtils
import re
from bs4 import BeautifulSoup

 
#访问起始网页需添加的请求头，不加的话，得不到完整的源代码（反爬）
base_headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9'
}
#请求视频下载地址时需要添加的请求头
download_headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'Referer':'https://mp.weixin.qq.com/s/SL11aj8ndwtoc5u81N7tNw',
	'Origin':'https://mp.weixin.qq.com',
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, sdch, br',
	'Accept-Language':'zh-CN,zh;q=0.8'
}

#res = requests.get(base_url,headers=base_headers)
#res.encoding = 'utf-8'
#html = res.text
#print('返回值===\n' + html)
 
url = 'https://mp.weixin.qq.com/s/SL11aj8ndwtoc5u81N7tNw'
res = urllib.request.urlopen(url).read()
print(type(res))
print(res.decode('utf-8'))
print(type(res.decode('utf-8'))) 
filename= url[-20:]
open(filename,'wb').write(url)#在写文件时，要写成bytes类型的文件‘wb’
# html=BeautifulSoup(response,'html.parser')
 
#print(html)
# res = requests.get('https://mp.weixin.qq.com/s/SL11aj8ndwtoc5u81N7tNw')
# res.encoding = 'utf-8'
 
 
# html_str= res.text
# bs_xml = BeautifulSoup(html_str)

# print(bs_xml.prettify())
 
 