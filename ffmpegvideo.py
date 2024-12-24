import os
from moviepy.editor import VideoFileClip, concatenate_videoclips


def conver_video_byffmpeg():
   
    origin_path = r"E:\v58\file_list.txt"
    new_path = r"E:\v58\output.mp4"
    os.system(f'ffmpeg -f concat -i "{origin_path}" -c copy "{new_path}"')

def conver_video_byMoviepy():

    # 设置文件夹路径
    folder_path = r"E:\v58"
    # 获取所有 MP4 文件
    mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
    # 按文件名排序
    mp4_files.sort()

    # 自定义顺序的文件名列表
    #custom_order = ["video1.mp4", "video2.mp4", "video3.mp4"]  # 这里替换为你的文件名

    # 创建视频剪辑列表
    #clips = [VideoFileClip(os.path.join(folder_path, f)) for f in custom_order if f in os.listdir(folder_path)]

    # 创建视频剪辑列表
    clips = [VideoFileClip(os.path.join(folder_path, f)) for f in mp4_files]

    # 合并视频
    final_clip = concatenate_videoclips(clips)
    # 输出合并后的文件
    final_clip.write_videofile("output.mp4")

conver_video_byffmpeg()