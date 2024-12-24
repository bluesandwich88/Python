#!/usr/bin/env python
# coding=utf-8
'''
Author: Kevin.Ching
Date: 2019-11-19 17:01:16
LastEditors: KevinCheng
LastEditTime: 2024-12-10 19:50:20
Email: lampard_cheng@hotmail.com
'''
import time
import shutil
import os
import requests
from lxml import etree
import json
import re
import subprocess

# 下载视频文件
def download(referer_url,quality,headers,ffmpeg_path,file_path):
    res_data = requests.get(referer_url, headers=headers)
    res_html = etree.HTML(res_data.text)
    # 获取当前视频的title
    try:
        title = res_html.xpath('//*[@id="viewbox_report"]/h1/span/text()')[0]
        title = title.replace(' ','')
        print("当前正在下载,", title)
    except:
        title = ''
        print("视频名为空,")
    # 获取视频信息
    pattern_video = '__playinfo__=(.*?)</script><script>'
    # 正则匹配
    match_video = re.search(pattern_video,res_data.text)
    # 提取出第1组匹配结果，并转为json
    video_info_temp = json.loads(match_video.group(1))
    print(f"视频信息:{video_info_temp}")
    video_infos = {}
    # 获取视频质量
    video_infos['quality'] = video_info_temp['data']['accept_description'][quality]
    # 获取视频时长
    video_infos['video_info'] = video_info_temp['data']['dash']['duration']
    # 获取视频链接
    video_infos['video_url'] = video_info_temp['data']['dash']['video'][quality]['baseUrl']
    # 获取音频链接
    video_infos['audio_url'] = video_info_temp['data']['dash']['audio'][quality]['baseUrl']
    # 计算视频时长
    video_time = int(video_infos.get('video_info', 0))
    video_minute = video_time // 60
    video_second = video_time % 60
    print('当前下载视频清晰度为{}，时长{}分{}秒'.format(video_infos.get('quality', 0), video_minute, video_second))
    print("视频下载开始：%s" % title)
    video_content = getVideRequest(referer_url, video_infos.get('video_url', 0),headers)
    print('%s\t视频大小：' % title, round(int(video_content.headers.get('content-length', 0)) / 1024 / 1024, 2), '\tMB')
    with open(file_path+'_'+'%s_video.mp4' % title, 'ab') as output:
        output.write(video_content.content)
    print("视频下载结束：%s" % title)
    print("音频下载开始：%s" % title)
    audio_content = getVideRequest(referer_url,  video_infos.get('audio_url', 0),headers)
    print('%s\t音频大小：' % title, round(int(audio_content.headers.get('content-length', 0)) / 1024 / 1024, 2), '\tMB')
    with open(file_path+'_'+'%s_audio.mp4' % title, 'ab') as output:
        output.write(audio_content.content)
    print("音频下载结束：%s" % title)
    # 使用ffmpeg合并视频音频
    print("视频合成开始：%s" % title)
    command = ffmpeg_path+' -i %s_video.mp4 -i %s_audio.mp4 -c copy %s.mp4 -y -loglevel quiet'
    print(command)
    subprocess.Popen(command)
    print("视频合成结束：%s" % title)
    time.sleep(10)
    os.system('del '+file_path + '_' + title+'_audio.mp4')
    os.system('del '+file_path + '_' + title+'_video.mp4')
    print("删除临时文件完成")
# 请求视频
def getVideRequest(referer_url, video_url, headers):
    print("referer_url:"+referer_url)
    print("video_url:"+video_url)
    headers.update({"Referer": referer_url})
    return requests.get(video_url, headers=headers)
if __name__ == '__main__':
    # 视频链接
    referer_url = 'https://www.bilibili.com/video/BV144i2YBE3F'
    # 视频质量，['高清 1080P', '高清 720P', '清晰 480P', '流畅 360P']
    quality = 0
    # 请求头
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    # ffmpeg.exe所在路径
    ffmpeg_path = 'ffmpeg'
    # 文件保存位置
    file_path = "/Users/chengzhiwen/Downloads/"
    download(referer_url, quality, headers, ffmpeg_path, file_path)


    # ffmpeg -i /Users/chengzhiwen/Downloads/video.mp4 -i /Users/chengzhiwen/Downloads/audio.mp4 -c:v copy -c:a aac -strict experimental output.mp4
