# coding=utf-8
from datetime import datetime, timedelta
# name = input('请输入姓名')
# givenname = 'kevin'
# familyname = 'cheng'
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.count('a'))
# print('hello, {0} {1}'.format(familyname,givenname))
# print(f'hello, 我姓{familyname}，名{givenname}')

# a = input('请输入a')
# b = input('请输入b')
# print(int(a) ** int(b))
# print(int(a) + int(b))
# print(int(a) - int(b))
# print(str(a) + str(b))
# print(float(a) + float(b))

# today = datetime.now()
# one_day = timedelta(days = 10)
# yesterday = today - one_day
# print('yesterday===' + str(yesterday))

import json
 
person = {
  'name': 'jack',
  'age': 15,
  'email': 'jack@litets.com'
}
 
 
print('dict：', person)
 
person_json = json.dumps(person) # 转换为json
 
print('json：', person_json)
 
# print('year===' + str(today.year))
# print('month===' + str(today.month))
# print('day===' + str(today.day))

# birthday = input('你的生日 (yyyy/mm/dd) ?')
# birthday_date = datetime.strptime(birthday, '%Y/%m/%d')
# print('你的生日是: ' + str(birthday_date))
# Accept: */*
# Accept-Encoding: identity
# Accept-Language: zh-CNzh;q=0.9
# Referer: https://www.bilibili.com/video/av42129640
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/78.0.3904.108 Safari/537.36
# Origin: https://www.bilibili.com
# Host: cn-zjhz-cu-v-04.acgvideo.com