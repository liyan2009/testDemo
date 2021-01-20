#! python3
#-*- coding:utf-8 -*-

'''
发送测试报告
'''
import HTMLTestRunner
from CommonLibrary.SetSuite import SetSuite
import os

if __name__ == '__main__':
    ss=SetSuite()
    suite=ss.getSuite()
    #获取发送报告所在的目录
    report=os.path.join(os.path.dirname(os.getcwd()),"WebAutomation\\result\\report.html")
    with open(report,"wb") as ft:
        runner=HTMLTestRunner.HTMLTestRunner(stream=ft,verbosity=2,title=u"测试报告",description=u"详细记录")
        runner.run(suite)
