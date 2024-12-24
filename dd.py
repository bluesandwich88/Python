# coding=utf-8
import requests,os,re

search_name = input('您想要爬取的视频关键字是？\n(输入完毕请按回车)：')
pages = 51 #设置爬取的总页数
video_path = r'./'#视频保存路径
for page in range(1,pages):#翻页循环
    url = ('https://search.bilibili.com/all?keyword='+search_name+'&single_column=0&page='+str(page)) #翻页循环设定
    r = requests.get(url)#GET请求访问网页
    content = r.text#解析网页源码
    links = re.findall(r'www.bilibili.com/video/av\d+',content)#使用正则表达式从源码中找到所有视频地址
    for link in links:#循环下载所有链接
        os.system('you-get -o %s %s' % (video_path,link))#调用you-get方法挨个下载该次循环的所有视频