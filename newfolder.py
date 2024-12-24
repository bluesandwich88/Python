import os

from pathlib import Path

# 获取当前用户的下载目录路径
downloads_path = str(Path.home() / "Downloads")


def create_folders(folder_names, base_path):
    """
    批量创建文件夹并指定路径
    """
    for folder_name in folder_names:
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{folder_name}' created at '{folder_path}'.")

# 要创建的文件夹名字列表
folder_names = ["01.死神代理篇（001-020）", "02.尸魂界潜入篇（021-041）", "03.尸魂界激斗篇（042-063）", "04.魂狩篇（064-091）", "05.尸魂界强袭篇（092-109）", "06.初现篇（110-127）", "07.日番谷先遣队奋斗篇（128-137）", "08.虚圈潜入篇（138-146）", "09.大虚之森篇（147-149）", "10.破面•激斗篇（150-167）", "11.新队长天贝辅助篇（168-189）", "12.虚圈十刃激斗篇（190-203）", "13.蹴鞠篇（204-205）", "14.过去篇（206-212）", "15.魂葬刑事篇（213-214）", "16.空座町守护篇（215-226）", "17.过渡故事篇（227-229）", "18.斩魄刀异闻篇（230-255）", "19.斩魄刀番外篇（256-265）", "20.十刃决战篇（266-287）", "21.空座町乱战篇（288-305）", "22.蓝染决战篇（306-310）", "23.番外篇（311-316）", "24.护庭十三队侵军篇（317-342）", "25.完现术篇（343-366）"]

# 指定基本路径
# base_path = '/'

# 批量创建文件夹
create_folders(folder_names, downloads_path)