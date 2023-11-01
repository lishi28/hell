# -*-coding:utf-8-*-
# @Time    :2023/10/178:45
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :parse.py
# @Software:PyCharm


import csv
def parse_csv(file):
    mylist=[]

    with open(file,'r',encoding="utf-8")as f:
        data=csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist


if __name__ == '__main__':
        data=parse_csv(r"c:\Users\henying\Desktop\datas.csv")
        print(data)
