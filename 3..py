# -*-coding:utf-8-*-
# @Time    :2023/10/98:27
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :3..py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# 打开Chrome浏览器
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")
driver.maximize_window()
# 点击设置按钮
driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]').click()

# 点击搜索设置
driver.find_element(By.LINK_TEXT, "搜索设置").click()
time.sleep(4)
# 设置每页结果数为20

driver.find_element(By.XPATH,'//*[@id="se-setting-3"]/span[2]/label').click()
time.sleep(4)
# 设置每页显示数为50
driver.find_element(By.XPATH,'//*[@id="se-setting-3"]/span[3]/label').click()
time.sleep(2)
# 点击保存设置
driver.find_element(By.XPATH,'//*[@id="se-setting-7"]/a[2]').click()
time.sleep(2)
# 点击确定
a=driver.switch_to.alert
print(a.text)
#alert.dimiss()取消
driver.switch_to.alert.accept()
#alert.send_keyd()输入框的

driver.quit()


