import os
new_path = "E:\output.mp4"
def conver_m3u8_tpmp4():
    origin_path = input('请输入视频地址：')
    # origin_path = "https://cloud-video.hkatv.vip/out/2641_1603961160_909952/index_1080p.m3u8?auth_key=1726860588-4290336641-0-c26a00de6a81ba038e1adf8850a65d11"
    os.system(f'ffmpeg -i "{origin_path}" -c copy "{new_path}"')

conver_m3u8_tpmp4()