import requests
import json
import re
from urllib.parse import urlparse, parse_qs
import pandas as pd

def extract_video_id(video_input):
    """
    提取视频ID，如果输入是视频URL，则解析并提取ID。
    """
    # 判断输入是否为数字（视频ID）
    if video_input.isdigit():
        return video_input
    else:
        # 解析URL，提取视频ID
        parsed_url = urlparse(video_input)
        query_params = parse_qs(parsed_url.query)
        path_segments = parsed_url.path.strip('/').split('/')
        # 检查路径中是否包含视频ID
        if 'video' in path_segments:
            index = path_segments.index('video')
            if index + 1 < len(path_segments):
                return path_segments[index + 1]
        # 如果在查询参数中
        elif 'aweme_id' in query_params:
            return query_params['aweme_id'][0]
        else:
            # 从URL中使用正则表达式提取数字
            video_id_match = re.search(r'/video/(\d+)', video_input)
            if video_id_match:
                return video_id_match.group(1)
            else:
                raise ValueError("无法从输入中提取视频ID，请检查输入是否正确。")

def read_cookie_from_file(file_path):
    """
    从指定的文件路径读取Cookie字符串。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        cookie = f.read().strip()
    return cookie

def get_douyin_comments(video_input, cookie):
    """
    获取抖音视频的所有评论信息，并导出为Excel文件。
    """
    video_id = extract_video_id(video_input)

    # 请求URL的基础部分
    base_url = "https://www.douyin.com/aweme/v1/web/aweme/detail/"

    # 请求参数
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "aweme_id": video_id,
        "cursor": "0",  # 起始光标
        "count": "50",  # 每页获取的评论数量，可以根据需要调整，最大值为50
        "item_type": "0",
        "insert_ids": "",
        "whale_cut_token": "",
        "cut_version": "1",
        "pc_client_type": "1",
        "version_code": "170400",
        "version_name": "17.4.0",
        "cookie_enabled": "true",
        "screen_width": "1920",
        "screen_height": "1080",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Chrome",
        "browser_version": "110.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "110.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "cpu_core_num": "8",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "50",
    }

    # 解析Cookie字符串为字典
    cookie_dict = {}
    for item in cookie.split(';'):
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookie_dict[key.strip()] = value.strip()

    # 从Cookie中获取必要参数
    params['webid'] = cookie_dict.get('webid', '')
    params['msToken'] = cookie_dict.get('msToken', '')
    params['verifyFp'] = cookie_dict.get('s_v_web_id', '')
    params['fp'] = cookie_dict.get('s_v_web_id', '')

    # 设置请求头
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': f'https://www.douyin.com/video/{video_id}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',  # 可以替换为您的浏览器User-Agent
    }

    # 使用解析后的Cookie字典
    cookies = cookie_dict

    data_list = []
    has_more = True
    cursor = "0"

    while has_more:
        params['cursor'] = cursor
        # 发送GET请求
        response = requests.get(base_url, headers=headers, params=params, cookies=cookies)

        # 检查响应状态码
        if response.status_code == 200:
            result_list = response.json()
            comments = result_list.get("comments", [])
            for comment in comments:
                user = comment.get('user', {})
                # 用户主页链接
                user_profile_url = f"https://www.douyin.com/user/{user.get('sec_uid', '')}"
                # 用户ID
                user_id = user.get('uid', '')
                # 用户名
                user_name = user.get('nickname', '')
                # 用户评论
                user_comment = comment.get('text', '')

                data = {
                    '用户主页': user_profile_url,
                    '用户ID': user_id,
                    '用户名': user_name,
                    '用户评论': user_comment
                }
                data_list.append(data)

            has_more = result_list.get("has_more", 0) == 1
            cursor = result_list.get("cursor", "0")
            print(f"已获取 {len(data_list)} 条评论...")
        else:
            print(f"请求失败，状态码：{response.status_code}")
            print(f"响应内容：{response.text}")
            break  # 发生错误，退出循环

    if data_list:
        # 将数据保存到Excel文件
        df = pd.DataFrame(data_list)
        df.to_excel('douyin_comments.xlsx', index=False)
        print(f"评论已保存到 douyin_comments.xlsx 文件中，共获取 {len(data_list)} 条评论。")
    else:
        print("未获取到任何评论。")

if __name__ == "__main__":
    video_input = input("请输入抖音视频的URL或视频ID：")
    cookie = read_cookie_from_file('cookie.txt')
    get_douyin_comments(video_input, cookie)
