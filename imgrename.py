
import os
from PIL import Image

def get_image_creation_date(image_path):
    """
    获取图片的创建日期
    """
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                # print(exif_data)
                # 获取创建日期
                creation_date = exif_data.get(36867)
                return creation_date
    except Exception as e:
        print(f"Error getting creation date for {image_path}: {e}")
        return None

def batch_rename_images(folder_path):
    """
    批量获取文件夹中所有图片的创建日期，并将其作为新名称
    """
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.heic', '.png', '.jpeg', '.gif')):
            image_path = os.path.join(folder_path, filename)
            creation_date = get_image_creation_date(image_path)
            #print(filename)
            if creation_date:
                print(creation_date)
                # 格式化创建日期作为新名称
                # new_name = creation_date.replace(":", "").replace(" ", "_") + os.path.splitext(filename)[1]
                # new_path = os.path.join(folder_path, new_name)

                # try:
                #     # os.rename(image_path, new_path)
                #     # print(f"Renamed '{filename}' to '{new_name}'.")
                #     # 使用 mv 命令重命名文件，保留文件元数据
                #     os.system(f"mv -n {os.path.join(folder_path, filename)} {os.path.join(folder_path, new_name)}")
                #     print(f"Renamed '{filename}' to '{new_name}'.")
                # except Exception as e:
                #     print(f"Error renaming '{filename}': {e}")

# 文件夹路径
folder_path = "imgtotest"

# 批量获取图片的创建日期并重新命名
batch_rename_images(folder_path)