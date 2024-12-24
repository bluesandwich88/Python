import os
import sys
import yt_dlp
from prettytable import PrettyTable
import tkinter as tk
from tkinter import filedialog
from yt_dlp.utils import DownloadError


# 获取运行时目录
if getattr(sys, 'frozen', False):
    # 打包后的临时目录
    base_path = sys._MEIPASS
else:
    # 未打包时的脚本目录
    base_path = os.path.dirname(os.path.abspath(__file__))

# 拼接 ffmpeg 的完整路径
ffmpeg_path = os.path.join(base_path, 'ffmpeg', 'bin', 'ffmpeg.exe')



# 创建Tkinter根窗口
root = tk.Tk()
root.withdraw()  # 不显示主窗口

def showtable(URL):
    # 创建表格
    table = PrettyTable()
    # 添加表头
    table.field_names = ["ID", "EXT", "RESOLUTION", "FPS", "CH", "FILESIZE", "TBR", "PROTO", "VCODEC", "VBR", "ACODEC", "ABR", "ASR", "MORE", "INFO"]
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
    data = info['formats']
    table.align = "c"

    for item in data:
        row = [
            item.get("format_id", ""),  # 映射表头字段，缺失填空
            item.get("ext", ""),
            item.get("resolution", ""),
            "" if item.get("fps", "") in ["", None] else round(float(item["fps"])),
            "" if item.get("audio_channels", "") in ["", None] else item["audio_channels"],
            "" if item.get("filesize", "") in ["", None] else f"{round(float(item["filesize"]) / 1024 /1024, 2)}MiB",
            item.get("tbr", ""),
            item.get("protocol", ""),
            item.get("vcodec", ""),
            item.get("vbr", ""),
            item.get("acodec", ""),
            item.get("abr", ""),
            item.get("asr", ""),
            item.get("format_note", ""),
            item.get("container", "")
        ]
        table.add_row(row)  # 添加行数据
    print(table)


def selfdownload():
    type = input('请选择类型, 1:视频，2:音频: ')
    val = input(f'请输入{"视频" if type == '1' else "音频"}地址：')
    save_path = filedialog.askdirectory(title="选择保存文件夹")
    v_quality = ''

    if not save_path:  # 如果用户未选择文件夹，则终止操作
        print("未选择保存位置，下载取消。")
        os._exit(0)
    else:
        print(f"下载保存到: {save_path}")
         
        if type == '1':
            # 视频
            video_type = input('请选择视频类型, 1:顶级，2:自定义: ')
            if video_type == '1':
                v_quality = 'bv+ba/b'
                # os.system(f'{tool_path} -f "bv+ba/b" --merge-output-format mp4 "{val}" --output "{save_path}/%(title)s-%(resolution)s.%(ext)s"')   
            elif video_type == '2':
                isCheck = input('是否需要看list, y:需要 n:不需要: ')
                if isCheck == 'y':
                    showtable(val)
                    # os.system(f'{tool_path} -f "{quality}+ba/b" --merge-output-format mp4 "{val}" --output "{save_path}/%(title)s-%(resolution)s.%(ext)s"')

                v_quality = f"{input('请输入视频编号：')}+ba/b"
            else:
                os._exit(0)
        else:
            # 音频
            v_quality = 'ba'
            # os.system(f'{tool_path} -f "ba" -x --audio-format mp3 "{val}" --output "{save_path}/%(title)s-%(id)s.%(ext)s"')

        ydl_opts = {
            'format': v_quality,  # 下载最佳视频和音频流，并合并
            'merge_output_format': "mp4" if type == '1' else "mp3",  # 合并为 mp4 格式
            'outtmpl': os.path.join(save_path, '%(title)s-%(resolution)s.%(ext)s'),  # 设置下载后文件的名称格式
            'ffmpeg_location': ffmpeg_path,  # 相对于程序所在目录的路径
        }
        # 使用 yt-dlp 下载视频
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([val])

     
if __name__ == "__main__":
    try:
        # yt-dlp 的下载逻辑
        # 你的代码内容
        selfdownload()
    except DownloadError as e:
        if "ffmpeg" in str(e):
            print("ERROR: ffmpeg 未安装，请参考文档进行安装！")
        else:
            print("ERROR:", e)
        sys.exit(1)

# 使用完后销毁 Tk 主窗口
root.destroy()




# https://www.youtube.com/watch?v=HAcoya_e0C8
# https://www.youtube.com/watch?v=l3Ey_k0-_Uc