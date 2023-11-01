# -*-coding:utf-8-*-
# @Time    :2023/10/1610:28
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :shipo.py
# @Software:PyCharm
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HTMLTestRunnerNew
from parameterized import parameterized,param
import ddt


# @ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问”Login“ 页面
        self.driver.get("http://192.168.2.14:8000")

    """
    1.@ddt.data ,括号中传递列表和元组
    2.传递两个列表，代表两个case
    3.每个用例有三个参数

    (1)代表用户名取值
    （2） 代表密码取值
    （3）代表登录成功与否：约定：0 为失败，1为成功
    """

    # @parameterized.expand(["admin","admin","0"],["admin","admin123456","1"])
    @ddt.data(["admin", "admin", "0"], ["admin", "admin123456", "1"])
    @ddt.name_func(lambda x: 'test_login')
    def test_method(self, username, password, status):
        """
        错误密码登录失败
        登录名
        """
        login_name = self.driver.find_element(By.ID, "inputUsername")
        login_name.clear()
        login_name.send_keys(username)
        # 登录密码
        login_pwd = self.driver.find_element(By.ID, "inputPassword")
        login_pwd.clear()
        login_pwd.send_keys(password)
        # 登录按钮
        login_btn = self.driver.find_element(By.XPATH, '/html/body/div/form/button')
        login_btn.click()

        if status == "0":
            # 登录后失败信息
            ele = self.driver.find_element(By.XPATH, '/html/body/div/form/p')
            self.assertIn(ele.text, self.driver.page_source)
        elif status == "1":
            print("登录成功！！")
        else:
            print("参数化状态只能为0和1")

class Login_page_OBJ():
    Username=(By.ID,'inputUsername')
    Password=(By.ID,'inputPassword')
    Login_button=(By.XPATH,'/html/body/div/form/button')
    Login_info_err=(By.XPATH,'/html/body/div/form/p')



class BasePage():
    def __init__(self,driver):
        self.driver = driver

# class LoginPage(BasePage):
#
#     def user_inport(self,sendkeys):
#         self.driver.find_element(By.ID,'inputUsername')
#
#     def ped_input (self,sendkeys):
#         self.driver.find_element(By.ID,'inputPassword')
#
#     def long_butter(self):
#         self.driver.find_element\
#             (By.XPATH,'/html/body/div/form/button').click
#     def Login_info_err(self):
#         self.driver.find_element\
#             (By.XPATH,'/html/body/div/form/p')


class Login_page(BasePage):
    def enter_username(self,usernname):
        ele=self.driver.find_element(*Login_page_OBJ.Username)
        ele.clear()
        ele.send_keys(usernname)
    def enter_password(self,password):
        ele = self.driver.find_element(*Login_page_OBJ.Password)
        ele.clear()
        ele.send_keys(password)
    def click_login_gutton(self):
        ele=self.driver.find_element(*Login_page_OBJ.Login_button)
        ele.clear()
    def login_err(self):
        ele=self.driver.find_element(*Login_page_OBJ.Login_info_err)

class LoginTestCase():
    def login_case_01(self):
        url='"http://192.168.2.10:8000"'
        username='admin'
        password='adnib123456'

        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(url)
        loginPage(driver).enter_username(username)

        loginPage(driver).enter_password(password)
        lodinPage(driver).click_login_button()

if __name__ == '__main__':
        unittest.main()