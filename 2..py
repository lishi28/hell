# -*-coding:utf-8-*-
# @Time    :2023/9/2717:14
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :2..py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

el_1=driver.find_element(By.CSS_SELECTOR,"#su")
print(el_1)
