import os
import shutil
from datetime import datetime

def get_creation_date(file_path):
    """
    获取文件的创建日期
    """
    return datetime.fromtimestamp(os.path.getctime(file_path))

def rename_video_files(directory):
    """
    批量重命名视频文件，并保留创建日期
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.mp4', '.mov')):
            file_path = os.path.join(directory, filename)
            creation_date = get_creation_date(file_path)
            new_filename = creation_date.strftime('%Y%m%d%H%M%S') + os.path.splitext(filename)[1]
            new_file_path = os.path.join(directory, new_filename)
            shutil.move(file_path, new_file_path)
            # 设置新文件的创建日期为原始创建日期
            os.utime(new_file_path, (os.path.getatime(new_file_path), os.path.getmtime(new_file_path), os.path.getctime(file_path)))

# 指定视频文件所在的目录
video_directory = 'path/to/your/video/directory'

rename_video_files(video_directory)
