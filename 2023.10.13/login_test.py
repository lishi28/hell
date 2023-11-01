# -*-coding:utf-8-*-
# @Time    :2023/10/178:44
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :1.py
# @Software:PyCharm
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HTMLTestRunnerNew
from parameterized import parameterized, param
import unittest
import ddt
import pytest

"""

安装DDT
pip install ddt -i https://pypi.tuna.tsinghua.edu.cn/simple

"""


#
#
# class TestLogin(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(20)
#         # 访问”Login“ 页面
#         self.driver.get("http://192.168.2.10:8000")
#
#     """
#     1.@ddt.data ,括号中传递列表和元组
#     2.传递两个列表，代表两个case
#     3.每个用例有三个参数
#
#     (1)代表用户名取值
#     （2） 代表密码取值
#     （3）代表登录成功与否：约定：0 为失败，1为成功
#     """
#
#     @parameterized.expand([("admin", "admin", "0"), ("admin", "admin123456", "1")])
#     def test_001_login(self, username, password, status):
#         """
#         错误密码登录失败
#         登录名
#         """
#         login_name = self.driver.find_element(By.ID, "inputUsername")
#         login_name.clear()
#         login_name.send_keys(username)
#         # 登录密码
#         login_pwd = self.driver.find_element(By.ID, "inputPassword")
#         login_pwd.clear()
#         login_pwd.send_keys(password)
#         # 登录按钮
#         login_btn = self.driver.find_element(By.XPATH, '/html/body/div/form/button')
#         login_btn.click()
#
#         if status == "0":
#             # 登录后失败信息
#             ele = self.driver.find_element(By.XPATH, '/html/body/div/form/p')
#             self.assertIn(ele.text, self.driver.page_source)
#         elif status == "1":
#             print("登录成功！！")
#         else:
#             print("参数化状态只能为0和1")
#
#     #
#     def tearDown(self) -> None:
#         self.driver.quit()


# class Login_Page_OBJ():
#     Username = (By.ID, "inputUsername")
#     Password = (By.ID, "inputPassword")
#     Login_button = (By.XPATH, '/html/body/div/form/button')
#
#     Login_info_err = (By.XPATH, '/html/body/div/form/p')
#
#
# class BasePage():
#
#     def __init__(self, driver):
#         self.driver = driver
#
#
# class LoginPage(BasePage):
#
#     def enter_username(self, username):
#         ele = self.driver.find_element(*Login_Page_OBJ.Username)
#         ele.clear()
#         ele.send_keys(username)
#
#     def enter_password(self, password):
#         ele = self.driver.find_element(*Login_Page_OBJ.Password)
#         ele.clear()
#         ele.send_keys(password)
#
#     def click_login_button(self):
#         ele = self.driver.find_element(*Login_Page_OBJ.Login_button)
#         ele.click()
#
#     def login_err(self):
#         ele = self.driver.find_element(*Login_Page_OBJ.Login_info_err)
#         print(ele.text)


#
#
#


import pandas as pd

data = pd.read_excel('asss.xls').values.tolist()

print(data)
class LoginTestCase(unittest.TestCase):
    @pytest.mark.parametrize(('username','password','status'),data)

    def test_login_case_01(self, username, password, status):

        url = "http://127.0.0.1:8000/"
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
    pytest.main(['-s'])
