# -*-coding:utf-8-*-
# @Time    :2023/10/1710:08
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :test_py.py
# @Software:PyCharm
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HTMLTestRunnerNew
from parameterized import parameterized, param
import pytest
from parse import parse_csv
import time




class Login_Page_OBJ():
    Username = (By.ID, "inputUsername")
    Password = (By.ID, "inputPassword")
    Login_button = (By.XPATH, '/html/body/div/form/button')

    Login_info_err = (By.XPATH, '/html/body/div/form/p')


class BasePage():

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def enter_username(self, username):
        ele = self.driver.find_element(*Login_Page_OBJ.Username)
        ele.clear()
        ele.send_keys(username)

    def enter_password(self, password):
        ele = self.driver.find_element(*Login_Page_OBJ.Password)
        ele.clear()
        ele.send_keys(password)

    def click_login_button(self):
        ele = self.driver.find_element(*Login_Page_OBJ.Login_button)
        ele.click()

    def login_err(self):
        ele = self.driver.find_element(*Login_Page_OBJ.Login_info_err)
        print(ele.text)


#
#
#


# import pandas as pd

data = parse_csv(r"c:\Users\henying\Desktop\datas.csv")

print(data)


@pytest.mark.parametrize(("username","password","status"), data)
class TestLoginTestCase():

    def test_login_case_01(self, username, password, status):

        url = "http://150.109.156.47:8000/add_event/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        time.sleep(2)
        LoginPage(self.driver).enter_username(username)
        time.sleep(2)
        LoginPage(self.driver).enter_password(password)
        time.sleep(2)
        LoginPage(self.driver).click_login_button()

        if status == "0":
            LoginPage(self.driver).login_err()
        else:
            print("success!!")
        # return  driver


if __name__ == '__main__':
    pytest.main(['-s',"test_py.py"])
