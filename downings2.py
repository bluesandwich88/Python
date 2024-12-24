#!/usr/bin/env python
# coding=utf-8
'''
Author: Kevin.Ching
Date: 2024-12-02 20:48:27
LastEditors: KevinCheng
LastEditTime: 2024-12-24 16:25:05
Email: lampard_cheng@hotmail.com
'''

#!/usr/bin/env python3
#coding=utf-8
import requests
import os
import json
import time

downloadNum = 0
# 替换为你的JSON文件路径
json_file_path = './weiboimg.json'
# 读取并解析JSON文件
with open(json_file_path, 'r') as file:
    imgData = json.load(file)
length = len(imgData)
print(f"The length of the data is: {length}")

base_headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Referer": "https://weibo.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
    "Connection": "keep-alive"
}

# url = 'https://ww1.sinaimg.cn/orj1080/5de52038tw1drgwvqxlztg.jpg'
save_dir = '/Users/chengzhiwen/Downloads/'

for item in imgData:

    try:
        # print(item)
        response = requests.get(f'https://ww1.sinaimg.cn/orj1080/{item}.jpg', headers=base_headers)
        # 获取图片文件名
        filename = os.path.join(save_dir, f'{item}.jpg')
        # print(response)

        # 将图片写入文件
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f'图片：{item} - 下载成功')
        downloadNum = downloadNum + 1
        print(f'已经下载了{downloadNum}张图片')
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code}")
    except Exception as e:
        print(f"Error: {e} - {obj['url']}")

    time.sleep(2)