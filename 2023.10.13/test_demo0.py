# -*-coding:utf-8-*-
# @Time    :2023/10/3014:45
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :test_demo0.py
# @Software:PyCharm
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HTMLTestRunnerNew
from parameterized import parameterized,param
import ddt
import time


class Tset(unittest.TestCase):
    def setUp(self) -> None:
        self.driver =webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://150.109.156.47:8000/")





    @ddt.data(['admin','admin',"0"],['admin','admin123456','1'])
    @ddt.name_func(lambda x:'test_login')
    def test_method(self):
            login_name=self.driver.find_element(By.XPATH,'//*[@id="inputUsername"]')
            login_name.click()
            login_name.send_keys(username)
            login_word = self.driver.find_element(By.XPATH,'//*[@id="inputPassword"]')
            login_word.click()
            login_word.send_keys(userword)

            login_aa =self.driver.find_element(By.XPATH,'/html/body/div/form/button')
            login_aa.click()

    def test_02(self):
        login_qq=self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/button')
        login_qq.click()
        time.sleep(3)
        #添加嘉宾
    def test_03(self):
        login_01=self.driver.find_element(By.XPATH,'//*[@id="id_name"]').send_keys('光明')


        login_02=self.driver.find_element(By.XPATH,'//*[@id="id_address"]').send_keys(123)


        login_03=self.driver.find_element(By.XPATH,'//*[@id="id_address"]').send_keys('')
        login_04=self.driver.find_element(By.XPATH,'//*[@id="id_start_time"]').send_keys()
    if __name__ == '__main__':
        unittest.main()




