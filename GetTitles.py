# -*- coding = utf-8 -*-

# 导入库
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

# 给对象添加功能
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 隐藏界面
options.add_argument('--mute-audio')  # 静音
options.add_argument('window-size=1920x1080')  # 防止无头模式加载页面不完整
options.add_argument('--start-maximized')  # 防止无头模式加载页面不完整
# 创建对象
driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=options)
flag = 1
titles = []

# 写入文件
def GetTitle():
    global flag
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    getTitle = soup.select('head > title')
    title = getTitle[0].text
    if title in titles:
        flag = 0
    else:
        titles.append(title)
        with open('filelist.txt', 'a', encoding='utf-8') as f:
            f.write(title + '\n\n')
        print(title + ' 加载完成！')

# 访问网页
BaseUrl = input('请输入drama链接：')
driver.get(BaseUrl)
driver.implicitly_wait(4)
sleep(2)

while flag:
    GetTitle()
    if flag == 0:
        break
    else:
        nextBtn = driver.find_element(By.ID,'mpinext')
        nextBtn.click()
        driver.implicitly_wait(4)
        sleep(2)
driver.quit()
print('所有标题已加载完成！请填写直链')