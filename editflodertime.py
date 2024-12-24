import os
import ctypes
from datetime import datetime

def modify_folder_creation_time(folder_path, creation_time):
    # 打开文件夹句柄
    folder_handle = ctypes.windll.kernel32.CreateFileW(
        folder_path, 256, 0, None, 3, 0x02000000, None
    )

    if folder_handle == -1:
        raise OSError("无法打开文件夹句柄")

    # 将时间转为 Windows 文件时间格式
    filetime = datetime_to_filetime(creation_time)

    # 设置文件夹的创建时间
    ctypes.windll.kernel32.SetFileTime(folder_handle, ctypes.byref(filetime), None, None)

    # 关闭文件夹句柄
    ctypes.windll.kernel32.CloseHandle(folder_handle)

def datetime_to_filetime(dt):
    # 将 datetime 对象转换为 Windows 文件时间格式
    epoch_as_filetime = 116444736000000000  # 1601-01-01 的 Windows 文件时间
    hundreds_of_ns = int(dt.timestamp() * 10000000)
    return ctypes.c_ulonglong(epoch_as_filetime + hundreds_of_ns)

# 使用示例
folder_path = r'E:\私人视频\《方太美食廣場》︱ATV'
new_creation_time = datetime(2022, 6, 8, 22, 53, 7)

modify_folder_creation_time(folder_path, new_creation_time)
