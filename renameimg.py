import os
import time
import win32file
import pywintypes
from datetime import datetime

# 指定图片所在的目录
image_directory = 'E:/私人照片/'

# 获取文件的创建日期
def get_creation_date(file_path):
    return datetime.fromtimestamp(os.path.getctime(file_path))

def get_edit_date(file_path):
    return datetime.fromtimestamp(os.path.getmtime(file_path))

def set_creation_time(file_path, creation_time):
    try:
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
    except pywintypes.error as e:
        print(f"Error setting creation time for {file_path}: {e}")
        return False
    return True

# 检查文件是否被锁定
def is_file_locked(file_path):
    try:
        # 尝试打开文件进行写操作，如果成功，文件未被锁定
        with open(file_path, 'a'):
            return False  # 文件未被锁定
    except IOError:
        return True  # 文件被锁定

# 重试机制，检测文件是否被锁定并尝试重新设置创建时间
def set_creation_time_with_retry(file_path, creation_time, max_retries=5, delay=1):
    retries = 0
    while retries < max_retries:
        if not is_file_locked(file_path):  # 文件没有被锁定，设置创建时间
            if set_creation_time(file_path, creation_time):
                # print(f"Successfully updated creation time for {file_path}")
                return True
        else:
            retries += 1
            # print(f"File {file_path} is locked, retrying... ({retries}/{max_retries})")
            time.sleep(delay)  # 等待一段时间后重试
    print(f"Failed to update creation time for {file_path} after {max_retries} retries.")
    return False

# 批量重命名图片，并保留创建日期
def rename_images(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.heic', '.dng', '.webp', '.gif', '.bmp')):
            
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
            set_creation_time_with_retry(new_file_path, mod_time)
            print(f"Renamed {filename} to {new_filename}")
            # time.sleep(0.5)  # 适当的延时，避免文件处理过于频繁

            # 创建时间（ctime）：表示文件或目录的创建时间，通常是在它们第一次被创建时设置。
            # 修改时间（mtime）：表示文件或目录的最后一次修改时间。当文件内容被修改或者目录下的文件被添加、删除或重命名时，修改时间会被更新。
            # 访问时间（atime）：表示文件或目录的最后一次访问时间。当文件被读取或目录被列出时，访问时间会被更新。
            # # 设置新文件的创建日期为原始创建日期
if __name__ == "__main__":
    rename_images(image_directory)
