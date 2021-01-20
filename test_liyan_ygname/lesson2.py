#_*_ coding:utf-8 _*_
import unittest
import requests
import json
import io
import sys
from test_lesson import get_formatted_name
'''
class NameTestCase(unittest.TestCase):
    def test_zdy(self):
        name=get_formatted_name('a','b')
        self.assertEquals(name,'a b')
unittest.main()
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("除数不能为0")
#读取文件内容
path=r'C:\test\1.txt'
def readfile():
    with open(path) as file_obj:
        content=file_obj.read()
        print(content.rstrip())
        '''for line in content:
            print(line.rstrip())
        '''
        '''
        for line in content:
            print(line)
        '''
def writefile():
    with open(path,'a') as file_obj:
        file_obj.write('hello world')
r=requests.get("http://www.baidu.com")
print(r.text)
print(r.status_code)
print(r.encoding)
heads={"Content-Type":"text/html; charset=UTF-8"}
res=requests.get("https://saas-api.mayitest.cn/user/users/get-refresh-info",params=heads)
print(res.headers)
print(res.text)
print(res.status_code)
if(res.status_code==requests.codes.ok):
    print("成功")


