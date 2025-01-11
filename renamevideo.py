import os
import time
import win32file
import pywintypes
from datetime import datetime



def set_creation_time(file_path, creation_time):
    # 获取文件句柄
    handle = win32file.CreateFile(
        file_path,
        win32file.GENERIC_WRITE,
        0,  # 不允许共享
        None,
        win32file.OPEN_EXISTING,
        0,
        None
    )
    
    # 将创建时间、修改时间和访问时间都设为指定的时间
    creation_time = pywintypes.Time(creation_time)
    win32file.SetFileTime(handle, creation_time, None, None)
    handle.close()



# 获取文件夹下所有文件

def rename_videos(folder_path): 
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 只处理 MP4 和 MOV 文件
        if os.path.isfile(file_path) and filename.lower().endswith(('.mp4', '.mov')):
 
            # 获取文件的修改时间
            mod_time = os.path.getmtime(file_path)

            # 转换为目标格式
            mod_time_formatted = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d_%H%M%S_%f')
            
            # 获取文件后缀
            file_ext = os.path.splitext(filename)[1].lower()
            
            # 生成新的文件名
            new_filename = f"{mod_time_formatted}{file_ext}"
            new_file_path = os.path.join(folder_path, new_filename)

            # 如果文件名已经存在，添加一个递增的数字后缀
            counter = 1
            while os.path.exists(new_file_path):
                new_filename = f"{mod_time_formatted}_{counter}{file_ext}"
                new_file_path = os.path.join(folder_path, new_filename)
                counter += 1
            # 重新命名文件
            os.rename(file_path, new_file_path)

            # 设置文件的创建时间为修改时间
            set_creation_time(new_file_path, mod_time)
            print(f"Renamed {filename} to {new_filename}")


if __name__ == "__main__":
    # 指定文件夹路径
    folder_path = r'E:\私人视频\iPhone视频\2023'
    rename_videos(folder_path)