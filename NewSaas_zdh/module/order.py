#! python3
#-*- coding:utf-8 -*-


import unittest
from module.login import LoginTestCase

class OrderInfo(object):

    def __init__(self):
        self.ln=LoginTestCase()
        self.driver=self.ln.test_loginFile()
        self.ln.getCookie()

    def test_order(self):
        mydriver=self.driver
        mydriver.get("https://i.mayitest.cn/#/user/dashboard")
        salary_menu=mydriver.find_element_by_css_selector("app-router-sidebar > div > ul > li.active > a > div")
        salary_menu.click()

orderinfo=OrderInfo()
orderinfo.test_order()