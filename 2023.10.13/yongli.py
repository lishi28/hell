# -*-coding:utf-8-*-
# @Time    :2023/10/3015:09
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :yongli.py
# @Software:PyCharm

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized
import ddt
import HTMLTestRunner

# Page class
class LoginPage:

  def __init__(self, driver):
  self.driver = driver

  def input_username(self, username):
  self.driver.find_element(By.ID, "username").send_keys(username)

  def input_password(self, password):
  self.driver.find_element(By.ID, "password").send_keys(password)

  def click_login(self):
  self.driver.find_element(By.ID, "submit").click()

# Base class
class BaseTest(unittest.TestCase):

  def setUp(self):
  self.driver = webdriver.Edge()

  def tearDown(self):
  self.driver.quit()

@ddt
class TestLogin(BaseTest):

  @parameterized.parameterized.dataprovider
  def test_login(self, username, password, expected):

  login = LoginPage(self.driver)
  login.input_username(username)
  login.input_password(password)
  login.click_login()

  if expected == "success":
    self.assertEqual(self.driver.title, "登录成功页面")
  else:
    self.assertIn("用户名或密码错误", self.driver.page_source)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
  outfile = open('report.html','wb')
  runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='测试报告',description='登录测试用例')
  runner.run(suite)
