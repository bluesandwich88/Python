#!/usr/bin/env python
# coding=utf-8
'''
Author: Kevin.Ching
Date: 2023-07-11 22:53:53
LastEditors: KevinCheng
LastEditTime: 2024-12-10 19:21:33
Email: lampard_cheng@hotmail.com
'''
import os
# from yt_dlp import YoutubeDL
tool_path = "yt-dlp"
save_path = "/Users/chengzhiwen/Downloads/"

def yt_donwload():
    val = input('请输入视频地址：')
    video_type = input('请选择视频类型, 1:顶级，2:自定义: ')

    if video_type == '1':     
        os.system(f'{tool_path} -f "bv+ba/b" --merge-output-format mp4 "{val}" --output "{save_path}%(title)s-%(resolution)s.%(ext)s"')   
    elif video_type == '2':
        isCheck = input('是否需要看list, y:需要 n:不需要: ')
        if isCheck == 'y':
            os.system(f'{tool_path} -F "{val}"')
        quality = input('请输入视频编号：')
        os.system(f'{tool_path} -f "{quality}+ba/b" --merge-output-format mp4 "{val}" --output "{save_path}%(title)s-%(resolution)s.%(ext)s"')    
    else:
        os._exit(0)

if  __name__ == '__main__' :
    yt_donwload()


# https://www.youtube.com/watch?v=maGISZFUH38