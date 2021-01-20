#! python3
#-*- coding:utf-8 -*-

import unittest
import HTMLTestRunner

import os


class TestHtmlRunner(unittest.TestCase):

    def test_01(self):
        self.assertEqual(3,3)

    def test_02(self):
        self.assertEqual(4,4)

    def tearDown(self):
        print("测试结束")

if __name__=='__main__':
    report="C:/Users/liyan/PycharmProjects/Selnium_SaasWeb/result/report.html"
    print(report)
    # ftp=open(report,'wb')
    suite=unittest.TestSuite()
    suite.addTest(TestHtmlRunner("test_01"))
    suite.addTest(TestHtmlRunner("test_02"))
    with open(report,'wb') as ftp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=ftp,title=u'测试报告')
        runner.run(suite)
    # ftp.close()
    # unittest.main()
