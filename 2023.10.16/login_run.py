# -*-coding:utf-8-*-
# @Time    :2023/10/1310:37
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :login_run.py
# @Software:PyCharm

import unittest
import HTMLTestRunnerNew

from login_13_01 import *
suite=unittest.defaultTestLoader.discover('.',pattern='login_13_01.py')

with open('reports.html','wb+') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(f,2,title
    ='测试报告',description='login reports',tester="Ervin")
    runner.run(suite)
