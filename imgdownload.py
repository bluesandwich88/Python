import os
import requests
import time
import datetime


def download_file_images(image_urls, save_dir):
    # 确保保存目录存在
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer": "https://www.photos18.com/zh-hans/v/EbORW",
        "Host": "img.photos18.com",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
        "Connection": "keep-alive"
    }
    for obj in image_urls:
        try:
            response = requests.get(url=obj['url'], headers=headers)
            response.raise_for_status()  # 检查请求是否成功
            
            # 获取图片文件名
            filename = os.path.join(save_dir, f'image_{obj['name']}.webp')
            print(response)
            # 将图片写入文件
            with open(filename, 'wb') as file:
                file.write(response.content)
            
            print(f'图片 {obj['name']} 下载成功: {filename}')
        
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e.response.status_code} - {obj['url']}")
        except Exception as e:
            file_list.append({
                "url": obj['url'],
                "name": obj['name']
            })
            print(f"Error: {e} - {obj['url']}")

        # 在 try 块中成功下载图片后添加延迟
        time.sleep(1)  # 等待 1 秒

    if file_list:
        print(f'失败列表：{file_list}')
        time.sleep(5)
        download_file_images(file_list, save_dir)
  
def download_single_images(save_dir):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://xx.knit.bid/ja/article/20230/",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
        "Connection": "keep-alive"
    }

    url = 'https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/aecc4233d5e1fbf78e754.jpg'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        
        # 获取图片文件名
    
        filename = os.path.join(save_dir, f'image_{int(datetime.datetime.now().timestamp())}.jpg')
        # print(response)
        # 将图片写入文件
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f'图片下载成功: {filename}')
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def download_muti_images(image_urls, save_dir):
    # 确保保存目录存在
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_list = [];
    print(f'下载图片总共 {len(image_urls)} 张')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://xx.knit.bid/ja/article/20230/",
        "Host": "xx-media.knit.bid",
        "Cookie": "cf_clearance=HbsAlSEVu3RLDxvXV4Al9DQ4Z5amjO5U5Tq93guYFjI-1729187728-1.2.1.1-OBy68aYScS7GwaCqeorImgxVlKw.wAiE92cikYHHUSGWUdqfV3GMynevrxCag_G4n67KW_1YxgIOKnITqav0QCDHmJzXqiiu77Z_qV1EVB0Ulf1zXVFamZsdrMcN3WBGZfcFotD6ZoHx6FNoCzspOvB4dsLdZ4Wo2V3dszrlRFpytValax0K_KBp6NQai224_Jzd.8AGPOvH0Hyvi_.TARRrVpE52AaQApNZTBkyNSlWn3Dbxk61E4oxkv_UjCkqsY_jnEANZNmX8YIlsuwIrsCCijqsspEI3DblBIrxUuDrS_WJYi8DhpbVHIGr2tpNWR3E3c8i_wxyQLsWr5o3aEVexoVgm4wW6EzFbcnmDpEuzGaeTYvZvajPkZPLVib0RJ7rL3ZrI1G.A7EZNKXpkQ",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
        "Connection": "keep-alive"
    }

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 检查请求是否成功
            
            # 获取图片文件名
            filename = os.path.join(save_dir, f'image_{i + 1}.jpg')
            # print(response)
            # 将图片写入文件
            with open(filename, 'wb') as file:
                file.write(response.content)
            
            print(f'图片 {i + 1} 下载成功: {filename}')
        
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e.response.status_code} - {url} - {i+1}")
        except Exception as e:
            # file_list.append({
            #     "url": url,
            #     "name": i+1
            # })
            print(f"Error: {e} - {url} - {i+1}")

        # 在 try 块中成功下载图片后添加延迟
        time.sleep(1)  # 等待 1 秒
    
    if file_list:
        print(f'失败列表：{file_list}')
        time.sleep(5)
        download_file_images(file_list, save_dir)

if __name__ == '__main__':
    # 示例图片地址数组
    #石川三郎石川澪-mio.dolミオドル84 P
    image_urls = [
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/aecc4233d5e1fbf78e754.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/58f1e2eaaea837c212e1a.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/6aea347e1dbbf3bc35af8.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/f6af89a8b15e895f1654f.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/18d90d00d9da74b469624.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/01c34007d40c19ca12a5f.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/b11bdeb3d23ff29773df9.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/9174bfa1150835e2b4d82.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/12a42a7222634646970aa.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/11600de36e914df23398a.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/d9ba1657495de2634edea.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/739f8084df3d001033403.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/0b5534921c95bc6812087.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/e7f69913bf6b4b13c7dd6.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/66686843352a4db0992bd.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/90e9d3949dc10a215a6f9.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/152f4a824b4f208233f4e.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/31a23b611cb5bc0b63837.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/0eaedc783e186520e80c3.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/e39268aa1fe60902526c9.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/2dfd2b86ad157c1e3fc40.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/fead98c3358003ed82074.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/c2a845bdce229cb9922bb.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/b5b21c39e1f279a45dbca.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/40933cc311112acb572a2.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/6b8cadf423b076fdf8fb6.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/151281e1578933cd2c1cb.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/94eeadf0df86f9e59f07e.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/d65ee9e760d4cd4d20821.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/5e95add05fce554209a03.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/0ae5434b03042d46c7c49.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/541d2ef14ae7c0ec65e6f.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/7a8d9c139442e63c9f2a9.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/35f071d99f2bd3836be69.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/7e1fa49df0862f28689ba.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/22b350f27ded116665737.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/b2374879492526ef89d58.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/c808c9e38fad69fc7c6ce.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/3aed1c272295af89d8caf.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/e698d55c852a4ac6d260c.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/3992f8369812d5fe4ab74.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/cbfe46a5afdcce6dbc588.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/50fe733b721acee15f858.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/3ada67ed91260502764e1.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/70335a059f754cb074023.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/8e2553530fefea98dd6b0.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/bdf764f7846a58cb620b4.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/a33de021ce62bbbc139d8.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/1af761704971c2fb12f96.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/29630f1a9e280ffc096c2.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/08ac37a5fbd303b1ebfcf.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/39d00a4ab8334c1204819.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/bb251503975a16d385d50.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/44135a7ec63fdc9fdc2a3.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/440de747adcbcb4c876c3.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/17858b8a4dcf86b545bdf.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/612ef8dba687d98d29720.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/a2431b672237a5c1af00e.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/92705b86a80ad8a5c0747.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/ece235abf2a5572fd0f38.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/e25f946f2a50e7d3c6679.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/b6f401d53c8d8db7de6e6.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/98630fcf6f3861ee6d943.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/25fd18c2607e44b79d642.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/07960b26e96633c6a8869.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/bbabac49310999a036835.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/25d84922037c63a8e8bb2.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/2b487eb2fbc04afb840a3.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/6d5e663d7800537366ede.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/3d088e19ff4261b89a8bc.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/6800f413f02e97836c2f2.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/a517d4b40377350e4a7e2.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/8c966a0def96b884b85d0.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/a27f43b488bc3dbac4195.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/9899db3de192711a0ceb5.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/0d6479d3ca1a730879b16.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/53656ea63b7fbdf0ebbd9.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/9d0e8585d5f50511ff200.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/b4fe1e1acb3c9383874be.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/78ca28dd4be2dae5d114a.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/e7a836f64c22017c564d5.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/fb2cc30d43a2ccdb09301.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/5d1e4fe004350a767a33e.jpg",
        "https://xx-media.knit.bid/static/images/2023/09/09/%5BPB%5D%20Mio%20Ishikawa%20%E7%9F%B3%E5%B7%9D%E6%BE%AA%20-%20Mio.dol%20%E3%83%9F%E3%82%AA%E3%83%89%E3%83%BC%E3%83%AB%2084P/fa1df4afecc300c3df9b4.jpg"
    ]
# 指定保存目录
save_dir = 'E:\\TDDOWNLOAD'

#download_muti_images(image_urls, save_dir):
download_single_images(save_dir)
#download_file_images(again_urls, save_dir)