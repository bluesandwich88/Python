import os
import datetime

def get_file_metadata(file_path):
    """
    获取文件的元数据
    """
    metadata = os.stat(file_path)
    return metadata

# 文件路径
file_path = "/path/to/your/file"

# 获取文件的元数据
file_metadata = get_file_metadata(file_path)

# 打印文件的元数据
print("File Metadata:")
print(f"File path: {file_path}")
print(f"Size: {file_metadata.st_size} bytes")
print(f"Creation time: {datetime.datetime.fromtimestamp(file_metadata.st_ctime)}")
print(f"Last modified time: {datetime.datetime.fromtimestamp(file_metadata.st_mtime)}")
print(f"Last access time: {datetime.datetime.fromtimestamp(file_metadata.st_atime)}")