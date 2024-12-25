#!/usr/bin/env python
# coding=utf-8
'''
Author: Kevin.Ching
Date: 2024-12-25 00:51:20
LastEditors: KevinCheng
LastEditTime: 2024-12-25 15:58:37
Email: lampard_cheng@hotmail.com
'''
import requests
import json

# 代理服务器的配置信息
proxyHost = "www.16yun.cn"
proxyPort = "5445"
proxyUser = "16QMSOML"
proxyPass = "280651"

# 构建代理字典，格式为：{'协议':'http://用户名:密码@代理服务器地址:端口'}
proxies = {
    'http': f'http://{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}',
    'https': f'https://{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}'
}

def get_video_title(video_id):
    # 抖音API的URL，这里仅为示例，请替换为实际的API URL
    url = f"https://api.tiktok.com/video_info?video_id={video_id}"

    # 构造请求头部，通常包括用户代理等信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://api.tiktok.com/'
    }

    # 发送请求，使用代理
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()  # 如果请求返回了不成功的状态码，将抛出异常
    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        print(f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        print(f'Timeout Error: {errt}')
    except requests.exceptions.RequestException as err:
        print(f'Error: {err}')

    # 解析响应内容
    data = response.json()

    # 提取视频标题
    title = data.get('title', 'No Title Available')

    return title

# 用示例视频ID调用函数
video_id = '7220634173042740538'
print(get_video_title(video_id))