import os
import ctypes
from ctypes import wintypes
from datetime import datetime

def set_file_modification_time(file_path, modification_time):
   
    # 将datetime对象转换为时间戳（秒）
    timestamp = int(modification_time.timestamp())
    

    # 修改文件的访问和修改时间
    os.utime(file_path, (timestamp, timestamp))

# 示例用法
##file_path = r"E:\私人视频\Chengli Tang's Wedding 2009-05-29.mp4"
file_path = r"D:\Documents\Videos\abc\SunQingHua&LiMengNi'sWedding2012-11-25.mp4"
modification_time = datetime(2012, 11, 25, 9, 12, 8)  # 设置为你想要的时间
set_file_modification_time(file_path, modification_time)
