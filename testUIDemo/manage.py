#! python3
#! -*- coding:utf-8 -*-

from BeautifulReport import BeautifulReport
from testCase.testLogin import TestLogin
from common.readConfig import ReadConfig
from common.sendEmail import SendEmail


import time
import os
import unittest

current_path=os.getcwd()
case_path=os.path.join(current_path,"testCase")
report_path=os.path.join("C:\\Users\\liyan\\PycharmProjects\\testUIDemo","testReport")

now=time.strftime("%Y-%m-%d-%H%M%S",time.localtime(time.time()))
report_title=u"测试报告"+now+".html"

def load_all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py")
    return discover

if __name__=="__main__":
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestLogin('test_pwdisnull'))
    # testsuite.addTest(unittest.makeSuite(TestLogin))
    run=BeautifulReport(testsuite)
    run.report(description=u"详细测试报告", filename=report_title,log_path=report_path)
    print("test")
    rc = ReadConfig()
    aa = rc.readConfig()
    mail_host=aa.get("EMAIL", "mail_host")
    mail_user = aa.get("EMAIL", "mail_user")
    mail_pwd = aa.get("EMAIL", "mail_pwd")
    mail_port = aa.get("EMAIL", "mail_host")
    receiver = aa.get("EMAIL", "receiver")
    subject = aa.get("EMAIL", "subject")
    content = aa.get("EMAIL", "content")
    maile_path = os.path.join(report_path, report_title)
    se = SendEmail()
    se.send_email(maile_path, mail_user,receiver, mail_pwd, content, mail_host, subject, report_title,"")
    # suit = unittest.TestSuite()
    # suit.addTest(TestLogin('test_pwdisnull'))
    # runner=unittest.TextTestRunner()
    # runner.run(suit)
