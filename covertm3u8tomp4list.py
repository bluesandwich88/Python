import os

# 批量下载和转换 m3u8 文件
def download_and_convert_m3u8_to_mp4(files_list, output_dir='/Users/chengzhiwen/Downloads/ouput'):
    # 检查输出文件夹是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    isKeep = True
    

    for file_info in files_list:

        if isKeep == True:
            url = file_info['url']  # 下载的 m3u8 链接
            output_name = file_info['name']  # 导出的文件名
            isKeep = False
            os.system(f'ffmpeg -i "{url}" -c copy "/Users/chengzhiwen/Downloads/ouput/{output_name}.mp4"')
            isKeep = True
        # 下载 m3u8 文件
        # m3u8_response = requests.get(url)
        # m3u8_file = os.path.join(output_dir, f"{output_name}.m3u8")
        
        # with open(m3u8_file, 'wb') as f:
        #     f.write(m3u8_response.content)

        # 使用 ffmpeg 将 m3u8 转换为 mp4
        # output_file = os.path.join(output_dir, f"{output_name}.mp4")
        # (
        #     ffmpeg
        #     .input(m3u8_file)
        #     .output(output_file, codec='copy')  # 使用 copy 模式直接转码，不重新编码
        #     .run(overwrite_output=True)
        # )
        #print(f"Downloaded and converted: {output_name}.mp4")

# 示例：批量下载和转换文件
files_list = [
    {
        "url": "https://cloud-video.hkatv.vip/out/3029_1603961516_092367/index_1080p.m3u8?auth_key=1728738098-2105979101-0-fff6e68ea1c67a1259901db952989c65",
        "name": "181"
    }
]


download_and_convert_m3u8_to_mp4(files_list)
