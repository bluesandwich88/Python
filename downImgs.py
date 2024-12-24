#!/usr/bin/python
# coding=UTF-8
import requests

imgList = []
base_headers = {
	'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebkit/605.1.15 (KHTML, like Gecko) Mobile/15E302 MicroMessenger/6.6.7 netType/WIFI Langguage/zh_CN',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9'
}
 
for i in range(194,221):
	imgList.append('https://big.diercun.com/hd1/Wanibooks/No.126/24meinv-'+str(i)+'.jpg')

imgNum = 194
for img in imgList:
	print('下载第'+str(imgNum)+'张图片')
	html = requests.get(img)
	path = "/Users/chengzhiwen/Downloads/newWanibooks WBGC/24meinv"+str(imgNum)+".jpg"
	with open(path,"wb")as f:
		f.write(html.content)
	imgNum+=1
if imgNum > 221:
	print('图片下载完成')