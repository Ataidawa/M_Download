# -*- coding = utf-8 -*-

# 导入要用的库
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import os
import json
import requests


# 给对象添加功能
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 隐藏界面
options.add_argument('--mute-audio')  # 静音
options.add_argument('window-size=1920x1080')  # 防止无头模式加载页面不完整
options.add_argument('--start-maximized')  # 防止无头模式加载页面不完整
# 创建对象
driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=options)

# 获取文件并保存
def GetFile(fileName,link):
    print(fileName + link)
    # 判断output文件夹是否存在
    if not os.path.exists('output'):
        os.mkdir('output')
    # 获取文件内容
    file = requests.get(link)
    # 写入并保存文件
    with open('./output/%s.m4a' % fileName, 'wb') as f:
        f.write(file.content)

# 获取网页信息
def GetScore(BaseUrl):
    global flag
    try:
        # 访问网站
        driver.get(BaseUrl)
        driver.implicitly_wait(4)
        sleep(3)
        # 保存该网页url，使其能够访问下一期页面
        thisUrl = driver.current_url
        # 获取文件名
        fileName = driver.find_element(By.CLASS_NAME, 'cover-title').text
        # 目前只考虑已完结的内容
        if '完结' in fileName:
            # flag用于控制循环，当下载完最后一期时结束循环
            flag = 0
        # 查找下载按钮
        download_btn = driver.find_element(By.ID, 'download-btn')
        download_btn.click()
        driver.implicitly_wait(4)
        sleep(1)
        # 获取link
        html_text = driver.page_source
        soup = BeautifulSoup(html_text, 'html.parser')
        # 通过检查元素检查是否仍然携带着cookies
        try:
            divs = soup.select('div[class="download-confirm-container"]')
            div = str(divs[0])
            link = div.split('"')[3]
            GetFile(fileName,link)
        except:
            # 发现没有携带cookies，携带Cookies重新访问
            with open('cookies.txt', 'r', encoding='utf8') as f:
                listCookies = json.loads(f.read())
            for cookie in listCookies:
                cookie_dict = {
                    'domain': '.missevan.com',
                    'name': cookie.get('name'),
                    'value': cookie.get('value'),
                    'path': '/',
                    'secure': cookie.get('secure')
                }
                driver.add_cookie(cookie_dict)
            # 携带完成后重新调用自己
            GetScore(BaseUrl)
        return thisUrl
    except:
        driver.quit()
        print('页面加载失败！')

# 核心内容
if __name__ == '__main__':
    # BaseUrl = 'https://www.missevan.com/sound/player?drama=5265'  # 使用播放列表网页作为基础链接
    BaseUrl = input('请输入猫耳FM-drama链接：')
    flag = 1  # 控制循环
    thisUrl = GetScore(BaseUrl)
    while flag:
        try:
            nextBtn = driver.find_element(By.ID,'mpinext')
            nextBtn.click()
            driver.implicitly_wait(4)
            sleep(2)
            GetScore(driver.current_url)
        except:
            print('点击 下一期 失败！')
            driver.quit()
    # 结束程序
    driver.quit()