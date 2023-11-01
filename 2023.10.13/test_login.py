# -*-coding:utf-8-*-
# @Time    :2023/10/3015:14
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :test_login.py
# @Software:PyCharm
import unittest
from time import sleep

from ddt import ddt, data
from selenium import webdriver


@ddt
class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Edge()
        self.driver.get('https://www.sogou.com/')

    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    # 单一参数
    @data('易烊千玺', '王嘉尔')
    def test_01(self, name):
        self.driver.find_element_by_id('query').send_keys(name)
        self.driver.find_element_by_id('stb').click()


if __name__ == '__main__':
    unittest.main()
