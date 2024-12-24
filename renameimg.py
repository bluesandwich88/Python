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
    image_dict = {}
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.heic', '.dng')):
            file_path = os.path.join(directory, filename)
            creation_date = get_creation_date(file_path)
            print(creation_date.strftime('%Y%m%d%H%M%S'))
            print(os.path.splitext(filename))
            new_filename = creation_date.strftime('%Y-%m-%d_%H%M%S') + os.path.splitext(filename)[1].lower()

            if new_filename in image_dict:
                # 如果文件名已经存在，则在文件名后添加序列
                image_dict[new_filename] += 1
                new_filename = new_filename.split('.')[0] + '_' + str(image_dict[new_filename]) + '.' + new_filename.split('.')[1]
            else:
               image_dict[new_filename] = 0
            new_file_path = os.path.join(directory, new_filename)
            shutil.move(file_path, new_file_path)
            # 设置新文件的创建日期为原始创建日期
            os.utime(new_file_path, (os.path.getmtime(new_file_path), os.path.getctime(new_file_path)))

            # 创建时间（ctime）：表示文件或目录的创建时间，通常是在它们第一次被创建时设置。
            # 修改时间（mtime）：表示文件或目录的最后一次修改时间。当文件内容被修改或者目录下的文件被添加、删除或重命名时，修改时间会被更新。
            # 访问时间（atime）：表示文件或目录的最后一次访问时间。当文件被读取或目录被列出时，访问时间会被更新。
            # new_file_path = os.path.join(directory, new_filename)
            # shutil.move(file_path, new_file_path)
            # # 设置新文件的创建日期为原始创建日期
            # os.utime(new_file_path, (os.path.getatime(new_file_path), os.path.getmtime(new_file_path)))

# 指定图片所在的目录 2023-02-12_140523.jpg
image_directory = 'e:/photo2023/'

rename_images(image_directory)
