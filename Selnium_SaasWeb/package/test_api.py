#! python3
# -*-coding:utf-8-*-

'''
@version:python3.6
@author:李艳
@software:pycharm
@time:2018.9.16
'''

#这里是从后台把数据写入到excel，方便半自动化

import requests
from package.common import Common
from urllib import parse
import logging
import re



class testApi(object):
    head = { 'Connection': 'keep-alive','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',"X-Requested-With":"XMLHttpRequest"}
    def __init__(self,method,url,data):
        self.url=url
        self.method=method
        #excel中设计的数据只能用单引号
        self.data=data
        # print(self.data)

    @property
    def testInterface(self):
        if self.method=="get":
            r=requests.get(self.url,params=self.data)
            print(r.url)
        elif self.method=="post":
            r=requests.post(self.url,data=self.data,headers=self.head)
            # print(r.cookies)
            # print(r.url)
            # print(r.cookies)
        return r


    #返回接口状态码
    @property
    def getCode(self):
        code=self.testInterface.status_code
        print(code)
        return code

    #返回status_code
    @property
    def getText(self):
        text=self.testInterface.text
        # print(text)
        return text

    #返回对比后的结果
    def  getResult(self,check_point,casename,log):
        r=self.testInterface
        status=r.status_code
        print(status)
        #resp=r.text.encode("unicode_escape").decode("unicode_escape")
        resp = r.json()
        result=""
        if(re.search(check_point,str(resp))):
            log.info("用例名称"+ casename +"接口执行成功！")
            result="success"
            return result,resp
        else:
            log.info("用例名称"+ casename +"接口执行失败！")
            result="fail"
            return result,resp



    #返回值中含有中文编码
    @property
    def getChange(self):
        r=self.testInterface
        text=r.text.encode("ISO-8859-1").decode("utf-8")
        print(text)
        return text

    #获取请求返回来的json数据
    # def getJson(self):
    #     json_data=self.testApi.json()
    #     return json_data

#
# mydata={'wd':'abc'}
# logingpostdata = parse.urlencode(mydata).encode('utf-8')
# ta = testApi("get","https://www.baidu.com",mydata)
# cc=ta.getChange
# log = Log("D:/autoAPI/log.txt")
# status,resp=ta.getResult("200","登录成功",log)
# print("aaaa")
# print(status,resp)
# 需要注意的事情是对比结果，并记录到文件内

