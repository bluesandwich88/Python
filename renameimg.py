import os
import shutil
import time
import win32file
import pywintypes
from datetime import datetime

# 指定图片所在的目录 2023-02-12_140523.jpg
image_directory = 'E:/2024/'

# 获取文件的创建日期
def get_creation_date(file_path):
    return datetime.fromtimestamp(os.path.getctime(file_path))

def get_edit_date(file_path):
    return datetime.fromtimestamp(os.path.getmtime(file_path))

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

# 批量重命名图片，并保留创建日期
def rename_images(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)


        if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.heic', '.dng', '.webp')):
            
            # 获取文件的修改时间
            mod_time = os.path.getmtime(file_path)

            # 转换为目标格式
            mod_time_formatted = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d_%H%M%S')
            
            # 获取文件后缀
            file_ext = os.path.splitext(filename)[1].lower()
            
            # 生成新的文件名
            new_filename = f"{mod_time_formatted}{file_ext}"
            new_file_path = os.path.join(directory, new_filename)


             # 如果文件名已经存在，添加一个递增的数字后缀
            counter = 1
            while os.path.exists(new_file_path):
                new_filename = f"{mod_time_formatted}_{counter}{file_ext}"
                new_file_path = os.path.join(directory, new_filename)
                counter += 1
            
            # 重新命名文件
            os.rename(file_path, new_file_path)

            # 设置文件的创建时间为修改时间
            set_creation_time(new_file_path, mod_time)
            print(f"Renamed {filename} to {new_filename}")


            # 创建时间（ctime）：表示文件或目录的创建时间，通常是在它们第一次被创建时设置。
            # 修改时间（mtime）：表示文件或目录的最后一次修改时间。当文件内容被修改或者目录下的文件被添加、删除或重命名时，修改时间会被更新。
            # 访问时间（atime）：表示文件或目录的最后一次访问时间。当文件被读取或目录被列出时，访问时间会被更新。
            # # 设置新文件的创建日期为原始创建日期
            # os.utime(new_file_path, (os.path.getatime(new_file_path), os.path.getmtime(new_file_path)))
    
if __name__ == "__main__":
    rename_images(image_directory)


# from PIL import Image
# import piexif
# from datetime import datetime

# def get_image_capture_date(image_path):
#     # 打开图片并提取 Exif 数据
#     image = Image.open(image_path)
#     exif_data = piexif.load(image.info["exif"])

#     # 获取 Exif 中的拍摄日期（`DateTimeOriginal`）
#     if piexif.ExifIFD.DateTimeOriginal in exif_data["Exif"]:
#         capture_date = exif_data["Exif"][piexif.ExifIFD.DateTimeOriginal].decode("utf-8")
#         print(f"拍摄日期1: {exif_data["Exif"][piexif.ExifIFD.DateTimeOriginal]}")
#         # 转换为 datetime 格式，保留毫秒
#         try:
#             capture_date = datetime.strptime(capture_date, "%Y:%m:%d %H:%M:%S")
#             return capture_date.strftime("%Y-%m-%d_%H:%M:%S")
#         except ValueError:
#             return "无法解析日期"
#     else:
#         return "没有拍摄日期"

# # 测试函数
# image_path = r'E:\私人图片\2024\2024-03-24_132542_928000.jpg'  # 替换为你图片的路径
# capture_date = get_image_capture_date(image_path)
# print(f"拍摄日期: {capture_date}")