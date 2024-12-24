import os
import shutil
from datetime import datetime


def get_creation_date(file_path):
    """
    获取文件的创建日期
    """
    return datetime.fromtimestamp(os.path.getctime(file_path))

def rename_images(directory):
    """
    批量重命名图片，并保留创建日期
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.heic', '.dng')):
            file_path = os.path.join(directory, filename)
            creation_date = get_creation_date(file_path)
            # print(creation_date.strftime('%Y%m%d%H%M%S'))
            # print(os.path.splitext(filename))
            print(get_creation_date(file_path))
            new_filename = creation_date.strftime('%Y') + '-' + creation_date.strftime('%m') + '-' + creation_date.strftime('%d') + '_' + creation_date.strftime('%H%M%S') + os.path.splitext(filename)[1]
            new_file_path = os.path.join(directory, new_filename)
             
            #shutil.move(file_path, new_file_path)
            # 设置新文件的创建日期为原始创建日期
            #os.utime(new_file_path, (os.path.getatime(new_file_path), os.path.getmtime(new_file_path)))

# 指定图片所在的目录 2023-02-12_140523.jpg
image_directory = 'imgtotest'

rename_images(image_directory)
