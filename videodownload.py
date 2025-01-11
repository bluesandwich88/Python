import requests

def download_video(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Referer': 'https://weibo.com/',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        with open(filename, 'wb') as out_file:
            out_file.write(response.content)
        print(f"Downloaded {filename} from {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {url}")
    except Exception as e:
        print(f"Error: {e} - {url}")

downloadUrL = input("请输入视频地址：")
 
#downloadUrL = "https://www.douyin.com/aweme/v1/play/?video_id=v0200fg10000c35gmnc5jmcf8osma4rg&line=0&file_id=eb99a6829a9c4fc78142294610bbd1cc&sign=630f67cb60b905c4e4a2b8733ac532f4&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL"
downloadUrL = downloadUrL.replace(" ", "").replace("\n", "")
if downloadUrL != '':
    download_video(downloadUrL, 'E:/TDDOWNLOAD/output2.mp4')
else:
    pass