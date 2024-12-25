#!/usr/bin/env python
# coding=utf-8
'''
Author: Kevin.Ching
Date: 2024-12-25 00:51:20
LastEditors: KevinCheng
LastEditTime: 2024-12-25 12:55:13
Email: lampard_cheng@hotmail.com
'''
import os
import requests
import subprocess
import tkinter as tk
from tkinter import filedialog

# 创建Tkinter根窗口
root = tk.Tk()
root.withdraw()  # 不显示主窗口


def get_headers_from_url(url):
    # 发起请求以获取响应头
 
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Referer': 'https://live.kankanews.com/'
    }


def conver_m3u8_tpmp4(url, save_path):
 
    if not save_path:  # 如果用户未选择文件夹，则终止操作
        print("未选择保存位置，下载取消。")
        os._exit(0)
    else:
        headers = get_headers_from_url(url)
        headers_str = f"User-Agent: {headers['User-Agent']}\r\nReferer: {headers['Referer']}"
        
        command = [
            'ffmpeg',
            '-headers', headers_str,
            '-i', url,        # 输入 m3u8 文件 URL
            '-c:v', 'libx264',      # 使用 x264 编码器
            '-c:a', 'aac',          # 使用 aac 音频编码器
            '-strict', 'experimental',
            '-f', 'mp4',            # 输出格式
            f"{save_path}/output_file.mp4",   # 输出文件名
            '-progress', '-',      # 在控制台实时显示进度
            '-nostats'             # 禁止冗余统计信息
        ]
        
        # 执行命令

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        for line in process.stdout:
            print(line.strip())  # 打印实时进度到控制台

        process.wait()
        print(f"Download and conversion completed! Saved as {save_path}")

if __name__ == "__main__":
    url = "https://4grhdymttga31hcjtgazdepbpq7314a5ecfzgh3mcqczgs45upiuo.wslivehls.com/ws-channels.kksmg.com/live/ylpd/playlist.m3u8?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOiJsaXZlIiwiZG9tYWluIjoid3MtY2hhbm5lbHMua2tzbWcuY29tIiwiZXhwIjoxNzM1MTI0MDg1LCJpYXQiOjE3MzUxMDI0ODUsIm5vbmNlIjoiZWd2d3QwM2kiLCJzdHJlYW1fbmFtZSI6InlscGQiLCJ1c2VyX2lkIjowLCJ1c2VyX2lwIjoiMjQwZTozODg6NmQwMjphYjAwOjJlMDo5N2ZmOmZlMWM6NmIzMyIsInV1aWQiOiI1TW93SW9RcHExTlY4c1F5cUZaZlkifQ.POJ27J8MJfQQvlSSLUCtxdNC4EB4aWqKwp3tsOQ9wxQ&wsSession=2a4015e57d72dac5e7b65cf1-173510248552722&wsIPSercert=a5ccd72b29c5fd46146a7f219914e80c&wsiphost=local&wsBindIP=1"
    save_path = filedialog.askdirectory(title="选择保存文件夹")
    conver_m3u8_tpmp4(url, save_path)


# 使用完后销毁 Tk 主窗口
root.destroy()