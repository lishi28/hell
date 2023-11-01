# -*-coding:utf-8-*-
# @Time    :2023/9/2616:59
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :1.py
# @Software:PyCharm

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.quit()#关闭