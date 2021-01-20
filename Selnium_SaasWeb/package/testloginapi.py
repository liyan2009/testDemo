#! python3
# -*-coding:utf-8 -*-


from package.common import Common
from package.test_api import testApi
from package.log import Log
from package.readConfig import ReadConfig
from package.sendEmail import SendEmail
from package.rwexcel import RWexcel
import os

import unittest
from package.HTMLTestRunner2 import HTMLTestRunner

'''
@content:主要进行具体接口测试调用
'''

class testLoginApi(unittest.TestCase):
    rf = ReadConfig()
    # def __init__(self):
    #     self.rf = ReadConfig()

    #使用xlrd和xlwr方式读取的excel信息
    def test_LoginApi(self):
        xls_name = "1.xls"
        sheet_name = "Sheet1"
        cn = Common(xls_name,sheet_name)
        baseUrl = self.rf.get_http("URL")
        excel=cn.get_Excel()
        rows=cn.get_rows
        cols=cn.get_cols
        url=cn.get_url
        method=cn.get_method
        data=cn.get_data
        dataType=cn.get_dataType
        checkData=cn.get_CheckData
        caseName = cn.get_caseName
        log=Log("D:/autoAPI/log.txt")
        print(baseUrl+url[1])
        for i in range(0,rows-1):
            api=testApi(method[i],baseUrl+url[i],eval(data[i]))
            if(method[i]=="post"):
                result=api.getResult(checkData[i],caseName[i],log)
                cn.update_sheetValue(result)
                # print(result)
            elif(method[i]=="get"):
                cc=api.getChange

    #使用openpyxl读取的excel信息,这个并保存了测试结果
    def test_MyLoginApi(self):
        xls_name = "2.xlsx"
        sheet_name = "Sheet1"
        cn = RWexcel(xls_name,sheet_name)
        baseUrl = self.rf.get_http("URL")
        rows=cn.get_Rows
        print(rows)
        # cols=cn.get_Columns
        url=cn.get_Url
        method=cn.get_Method
        data=cn.get_Data
        # dataType=cn.get_DataType
        checkData=cn.get_CheckData
        caseName = cn.get_CaseName
        log=Log("D:/autoAPI/log.txt")
        # print(baseUrl+url[1])
        for i in range(0,rows-1):
            api=testApi(method[i],baseUrl+url[i],eval(data[i]))
            if(method[i]=="post"):
                result,resp=api.getResult(checkData[i],caseName[i],log)
                cn.update_resultAndContent(i,result,resp)
            elif(method[i]=="get"):
                cc=api.getChange
        cn.save_Excel


# tapi=testLoginApi()
# bb=tapi.test_MyLoginApi()
# rc=ReadConfig()
# attach_xlsx='C:/Users/liyan/PycharmProjects/Selnium_SaasWeb/result/report.html'
# attach_jpg='D:\\autoAPI\\1.jpg'
# baseUrl=rc.get_http("URL")
# sender=rc.get_email("mail_user")
# receiver=rc.get_email("receiver")
# pwd=rc.get_email("mail_pwd")
# mailhost=rc.get_email("mail_host")
# subject=rc.get_email("subject")
# content=rc.get_email("content")
# filename="report.html"
# se=SendEmail()
# se.send_email(attach_xlsx,attach_jpg,sender,receiver,pwd,content,mailhost,subject,filename)

if __name__=='__main__':
    report=os.path.join("../result/report.html")

    ftp=open(report,'wb')
    suite=unittest.TestSuite()
    # suite.addTest(testLoginApi("test_LoginApi"))
    suite.addTest(testLoginApi("test_MyLoginApi"))
    # runner=HTMLTestRunner(stream=ftp,title=u'测试报告')
    # runner.run(suite)
    unittest.main()

