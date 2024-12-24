import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 启动Chrome浏览器
driver = webdriver.Chrome()
# 打开华为商城
url = "https://www.vmall.com/index.html"
driver.get(url)
driver.maximize_window()  # 窗口最大化

# 人工登录华为商城
# ...

# 打开要购买商品的页面
product_url = "https://www.vmall.com/product/10086499369393.html"  # Mate60产品ID
driver.get(product_url)

# # 设置抢购时间
start_time_str = "2024-9-25 10:07:50"
start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
end_time = start_time + datetime.timedelta(seconds=180)  # 抢购截止时间设置为3分钟后

# 开始抢购
while True:
    now = datetime.datetime.now()
    if now >= start_time:
        while True:
            print('重试1')
            try:
                # driver.find_element(By.LINK_TEXT, "立即下单").click()
                # driver.find_element(By.LINK_TEXT, "即将开始").click()
                element = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n']//div[text()='立即购买']")
                element.click()
                print('点击到-立即购买')
                break
            except:
                now = datetime.datetime.now()
                if now > end_time:
                    print('卡在立即购买')
                    break
                else:
                    pass
        
        while True:
            print('重试2')
            try:
                #driver.find_element(By.LINK_TEXT, "提交订单").click()
                ele = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n']//div[text()='提交订单']")
                ele.click()
                # print("抢到啦！！！快去支付")
                # driver.find_element(By.LINK_TEXT, "即将开始").click()
                print('点击到-提交订单')
                break
            except:
                now = datetime.datetime.now()
                if now > end_time:
                    print('卡在支付')
                    break
                else:
                    pass
        break

# 支付操作需要人工完成