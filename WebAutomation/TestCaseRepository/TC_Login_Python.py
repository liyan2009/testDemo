#! python3
#-*- coding:utf-8 -*-

import unittest
from WebPages.LoginPage import LoginPage
import time
import HTMLTestRunner
import os
from CommonLibrary.TestCaseInfo import  TestCaseInfo

class TC_Login_Python(unittest.TestCase):


    def setUp(self):
        self.baseUrl="https://i.mayitest.cn/#/entry/login"
        #用例路径
        self.testcaseInfo=TestCaseInfo(id=1,name="测试登录")


    def test_login(self):
        lp= LoginPage()
        lp.open(self.baseUrl)
        lp.login("13641878483","1234567")
        time.sleep(2)
        title=lp.getTitle()
        self.assertEqual(title,"首页")
        self.testcaseInfo.result="Pass"

    def test_case01(self):
        print("bbb")


    '''
    @des :一次性运行所有的用例
    '''
    def allCase(self):
        case_path=os.path.join(os.getcwd())
        discover=unittest.defaultTestLoader.discover(case_path,pattern="TC*.py",top_level_dir=None)
        return discover

    '''
    发送测试报告
    '''
    def run_allCases(self):
        report = os.path.join(os.path.dirname(os.getcwd()), 'result\\report.html')
        ftp=open(report,'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=ftp,title=u"测试报告",description=u"用例执行情况")
        runner.run(self.allCase())
        ftp.close()

    '''
    选择指定的用例进行执行
    '''
    def run_chooseCases(self):
        report=os.path.join(os.path.dirname(os.getcwd()), 'result\\report.html')
        ftp=open(report,'wb')
        suite=unittest.TestSuite()
        suite.addTest(TC_Login_Python("test_login"))
        with open(report,'wb') as ftp:
            runner=HTMLTestRunner.HTMLTestRunner(stream=ftp,title=u'测试报告',description=u"用例执行情况")
            runner.run(suite)

# if __name__=="__main__":
#     tc=TC_Login_Python()
#     tc.run_allCases()

