import os
import datetime
 
def rename_files(folder_path, replace_char):
    """
    将文件名中最后一个下划线替换为指定符号
    """
    for filename in os.listdir(folder_path):
        if "_" in filename:
            # print(filename.rsplit("_", maxsplit=1)[0])


            # new_filename = filename.split("_")[0] + filename.split("_")[1] + filename.split("_")[2] + '_' + filename.split("_")[3] + filename.split("_")[4]
            # print(new_filename)

            # print(filename.split("_"))
            # new_filename = filename.rsplit("_", maxsplit=1)[0] + replace_char + filename.rsplit("_", maxsplit=1)[1]
            # old_path = os.path.join(folder_path, filename)
            # new_path = os.path.join(folder_path, new_filename)
            # os.rename(old_path, new_path)
            # print(f"Renamed '{filename}' to '{new_filename}'.")
            return

 
# 文件夹路径
folder_path = "testimg"

# 要替换的符号
replace_char = ""

# 修改文件名
rename_files(folder_path, replace_char)

# 2023_01_01_19_00_IMG7085