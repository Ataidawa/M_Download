# -*- coding = utf-8 -*-
# 导入库
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import json

# 创建对象
driver = webdriver.Chrome(service=Service("./chromedriver.exe"))

# 访问网页
driver.get('https://www.missevan.com/member/login')
driver.implicitly_wait(4)
print('您有一分钟的时间登录哦~')
print('填写完成后不要操作页面哦，可以最小化窗口！')
# 等待登录（60s)
sleep(60)

# 获取Cookies
dictCookies = driver.get_cookies()  # 获取list的cookies
jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

# 写入文件
with open('cookies.txt', 'w', encoding='utf-8') as f:
    f.write(jsonCookies)
print('cookies保存成功！')
driver.quit()