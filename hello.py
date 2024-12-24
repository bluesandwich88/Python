#!/usr/bin/env python
# coding=utf-8
'''
Author: Kevin.Ching
Date: 2019-06-27 16:34:46
LastEditors: KevinCheng
LastEditTime: 2024-12-24 16:24:34
Email: lampard_cheng@hotmail.com
'''
#!/usr/bin/env python3
# coding=UTF-8
#!/usr/bin/python3
import requests
import os
import json
import time

downloadNum = 0
# 替换为你的JSON文件路径
json_file_path = './do.json'
# 读取并解析JSON文件
with open(json_file_path, 'r') as file:
    imgData = json.load(file)
    
    # 遍历数组并打印 key 值和内容
    for key, value in enumerate(imgData):
        print(f"Key: {key}, Value: {value['name']}")

 
    # 筛选 age 大于 30 的对象
    filtered_by_age = [item for item in imgData if item["age"] >= 40]
    print(f"筛选结果：{filtered_by_age}")

    
str='Abcdefg'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[-3]) 
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
input("\n\n按下 enter 键后退出。")
