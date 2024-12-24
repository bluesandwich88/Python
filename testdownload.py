import requests

def download_image(url, filename, proxies=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Referer': url,
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        
        with open(filename, 'wb') as out_file:
            out_file.write(response.content)
        print(f"Downloaded {filename} from {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {url}")
    except Exception as e:
        print(f"Error: {e} - {url}")

# 使用示例：带代理下载图片
proxies = {
    'http': 'http://127.0.0.1:7897/'
}
download_image("https://xx-media.knit.bid/static/images/2024/03/22/%E3%80%8E%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%A0%E3%83%8C%E3%83%BC%E3%83%89%E3%83%9D%E3%83%BC%E3%82%BA%E3%83%96%E3%83%83%E3%82%AF%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%E3%80%8F/11373572vmzrlymnlh.jpg", "image.jpg", proxies=proxies)
