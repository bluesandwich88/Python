 
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 启动Chrome浏览器

#driver = webdriver.Chrome (executable_path ="chromedriver/chromedriver.exe")
# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开华为商城
url = "https://www.vmall.com/index.html"
driver.get(url)
driver.maximize_window()  # 窗口最大化

# 人工登录华为商城
# ...

# 打开要购买商品的页面
product_url = "https://www.vmall.com/product/comdetail/index.html?prdId=10086063465292&sbomCode=3105020008101"  # Mate60产品ID
driver.get(product_url)
time.sleep(5)
print('休息结束')


start_time_str = "2024-9-23 10:07:50"
start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
end_time = start_time + datetime.timedelta(seconds=180)  # 抢购截止时间设置为3分钟后

while True:
    print('重试1')
    try:
        element = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n']//div[text()='立即购买']")
        #element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-1dbjc4n']//div[text()='即将开始']"))) 
        element.click()
        # driver.find_element(By.LINK_TEXT, "优惠").click()
        # driver.find_element(By.LINK_TEXT, "即将开始").click()
        print('点击到-立即下单')
        break
    except:
        now = datetime.datetime.now()
        if now > end_time:
            print('卡在立即下单')
            break
        else:
            pass
# try:
#     element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-1dbjc4n']//div[text()='立即购买']"))) 
#     element.click()
#     # driver.find_element(By.LINK_TEXT, "优惠").click()
#     # driver.find_element(By.LINK_TEXT, "即将开始").click()
#     print('点击到-立即下单')
#     time.sleep(60)
# except Exception as e:
#     print(f"未找到按钮或点击失败: {e}")

# driver.quit()
 