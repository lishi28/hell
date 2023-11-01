# -*-coding:utf-8-*-
# @Time    :2023/10/1715:07
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :demo_pytest.py
# @Software:PyCharm

import pytest

#
#
# class TestDemo():
#     def test_01(self):
#         print('aaa')
#         assert 'a'=='a'
#
#     def test_02(self):
#         print('bbb')
#         assert 'b'=='bb'
# if __name__ == '__main__':
#     pytest.main('-s','demo_pytest.py')


# def test_01():
#         print("aaaa")
#         assert "a"=="a"
# def test_02():
#         print("bbbb")
#         assert  'b' =='b'
# if __name__ == '__main__':
#     pytest.main('-s','demo_pytest.py')



"""
pytest 固件
setup  teardown

setup teardown  在调用方法前/后执行

setup_method/teardown_method     在类种的方法前，后执行

setup_class/ teardown_class 
在类的开始和结束执行

steup_function/teardown_function 
只对函数生效，不在类中

setup_module /teardown_miudle 用于模块
的始末，只执行一次，全局方法


"""


"""
在函数中使用

setup_function/teardown_function 只对函数生效。不在类中
在每个函数开始/末尾执行

setup_module /teardown_moudle 用于模块的始末，只执行一次，全局方法


"""

def setup_module():
    print('setup_module')
def teadown_module():
    print('teardown_module')
def setup_fuction():
    print('setup_fuction')
def teardown_function():
    print("teardown_function")

def test_01():
        print("aaaa")

        assert "a"=="a"
def test_02():
        print("bbbb")
        assert "b" == "b"
if __name__ == '__main__':
    pytest.main(["-s","demo_pytest.py"])

("\n"
 "class 中的测试固件\n"
 "\n"
 "\n"
 "setup_method/teardown_method     在类种的方法前，后执行,\n"
 "每个方法开始和前后执行\n"
 "setup_class/ teardown_class \n"
 "在类的开始和结束执行\n"
 "\n"
 "\n"
 "\n"
 "\n")
#


