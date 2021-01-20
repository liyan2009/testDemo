#! python3
#! -*- coding:utf-8 -*-

from pageObject.loginPage import LoginPage
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from common.readYaml import ReadYaml
from BeautifulReport import BeautifulReport
import time
import os

class TestLogin(unittest.TestCase):

    def setUp(self):
        url = ""
        self.driver = webdriver.Chrome()
        self.lp = LoginPage(self.driver, url)
        self.action = ActionChains(self.driver)
        self.r = ReadYaml()
        self.data = self.r.readFile("testData\login.yaml")

    #密码为空
    def test_pwdisnull(self):
        self.lp.click_wx(self.action)
        self.lp.user_login(self.data["case1"]["username1"],self.data["case1"]["pwd1"])
        pwd_text = self.lp.login_error_pwd()
        # print(pwd_text)
        self.assertEqual("密码不能为空","密码不能为空")
        # print("密码为空")

    #手机号为空
    def test_userisnull(self):
        self.lp.click_wx(self.action)
        self.lp.user_login(self.data["case2"]["username2"],self.data["case2"]["pwd2"])
        user_text=self.lp.login_error_user()
        self.assertEqual(user_text,"手机号码不能为空")
        # print("手机号码为空")

    #手机号为空或密码错误
    def test_useriserror(self):
        self.lp.click_wx(self.action)
        self.lp.user_login(self.data["case3"]["username3"],self.data["case3"]["pwd3"])
        user_text=self.lp.login_error_user()
        pwd_text = self.lp.login_error_pwd()
        self.assertEqual(pwd_text,"密码不能为空")
        self.assertEqual(user_text,"手机号码不能为空")
        # print("手机号或密码为空")

    #成功登录
    def test_login(self):
        self.lp.click_wx(self.action)
        self.lp.user_login(self.data["case4"]["username4"],self.data["case4"]["pwd4"])
        # print("正常登录")

    def tearDown(self):
        self.driver.close()

#
#
# if __name__=="__main__":
#     suit = unittest.TestSuite()
#     suit.addTest(TestLogin('test_pwdisnull'))
#     # suit.addTest(TestLogin('test_userisnull'))
#     # suit.addTest(TestLogin('test_useriserror'))
#     # suit.addTest(TestLogin('test_login'))
#     #
#     # now=time.strftime("%Y-%m-%d %H-%M-%S")
#     # file_name=now+"TestResult.html"
#     # result=BeautifulReport(suit)
#     # report_path=os.path.join(os.getcwd(),"testReport")
#     # print(report_path)
#     # result.report(filename=file_name,description='测试报告',log_path=report_path)
#
#
#     runner=unittest.TextTestRunner()
#     runner.run(suit)

# url=""
# driver=webdriver.Chrome()
# lp=LoginPage(driver,url)
# action=ActionChains(driver)
# tl=TestLogin()
# tl.test_login1("17308032045","1234567",action,lp)