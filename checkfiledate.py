import os
import datetime

def get_creation_date(file_path):
    # 获取文件的创建日期
    creation_timestamp = os.path.getctime(file_path)
    creation_date = datetime.datetime.fromtimestamp(creation_timestamp)
    return creation_date

def batch_get_creation_dates(folder_path):
    """
    批量获取文件夹中所有文件的创建日期
    """
    file_creation_dates = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            creation_date = get_creation_date(file_path)
            file_creation_dates[filename] = creation_date
    return file_creation_dates

# 文件夹路径
folder_path = "testimg"

# 批量获取文件的创建日期
file_creation_dates = batch_get_creation_dates(folder_path)

# 打印结果
for filename, creation_date in file_creation_dates.items():
    print(f"File '{filename}' created on: {creation_date}")
