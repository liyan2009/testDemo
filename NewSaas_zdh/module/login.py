#! python3
# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains

class LoginTestCase(object):

    def __init__(self):
        self.driver=webdriver.Chrome()

    #登录
    def test_loginFile(self):
        browser=self.driver
        browser.get("https://i.mayitest.cn")
        browser.implicitly_wait(4)
        #鼠标点击标签页
        yg=browser.find_element_by_xpath("//div[@class='login-box']/div[@class='box']/ul[@class='tabs clearfix']/li[2]/div")
        sleep(2)
        ActionChains(browser).move_to_element(yg).click(yg).perform()
        sleep(2)
        userElem=browser.find_element_by_xpath("//input[@formcontrolname='mobile']")
        userElem.clear()
        userElem.send_keys("13145866825")
        pwdElem = browser.find_element_by_xpath("//input[@formcontrolname='password']")
        pwdElem.clear()
        pwdElem.send_keys("1234567")
        btnLogin=browser.find_element_by_css_selector("div.login-box > div.box > form > button").click()
        sleep(4)
        browser.add_cookie({"name": "mayihr_token","value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vc2Fhcy1hcGkubWF5aXRlc3QuY24vdXNlci91c2Vycy9hdXRoZW50aWNhdGUiLCJpYXQiOjE1NzI0MjY4NjAsImV4cCI6MTU3MjU5OTY2MCwibmJmIjoxNTcyNDI2ODYwLCJqdGkiOiJ2R1R1Y0VyNmRZaEVPUHhJIiwic3ViIjo3NzMxNSwicHJ2IjoiZjkzMDdlYjVmMjljNzJhOTBkYmFhZWYwZTI2ZjAyNjJlZGU4NmY1NSIsImp3dF91c2VyX3R5cGUiOiJhcGkiLCJsb2dpbl9jbGllbnQiOiJwYyJ9.Gdo0i1l2HvrBniKkmYtyEvqZ1RRlTSfq2IjPJP8Ye9c"})
        # browser.refresh()
        sleep(3)
        return browser

    #获取cookie
    def getCookie(self):
        # for cookie in self.driver.get_cookies():
        #     # print(cookie["name"],cookie["value"])
        #     if cookie['name']=="gr_user_id":
        #         self.driver.add_cookie({"name": cookie['name'], "value": cookie['value']})
        #         webcookie=cookie['value']
        webcookie=self.driver.add_cookie({"name": "mayihr_token", "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vc2Fhcy1hcGkubWF5aXRlc3QuY24vdXNlci91c2Vycy9hdXRoZW50aWNhdGUiLCJpYXQiOjE1NzI0MjE0NjAsImV4cCI6MTU3MjU5NDI2MCwibmJmIjoxNTcyNDIxNDYwLCJqdGkiOiJtbGpVamQ1R0dDSjl5NWltIiwic3ViIjo3NzMxNSwicHJ2IjoiZjkzMDdlYjVmMjljNzJhOTBkYmFhZWYwZTI2ZjAyNjJlZGU4NmY1NSIsImp3dF91c2VyX3R5cGUiOiJhcGkiLCJsb2dpbl9jbGllbnQiOiJwYyJ9.5on91qwXFXtQ2PlAxWfChbnU8lsKVAJ-tA4sm8CWvIs"})
        return  webcookie

    #获取token
    # def get_token(self):
    #     token = self.driver.execute_script('localStorage.getItem("mayihr_token");')
    #     # 添加token
    #     # js = 'window.localStorage.setItem("token","token值")'
    #     # self.driver.execute_script(js)
    #
    #     # self.driver.refresh()  # 刷新
    #     return token

    #检查元素是否存在
    def isElementExist(self,element):
        flag=False
        browser = self.driver
        try:
            browser.find_element_by_css_selector(element)
            flag = True
            return flag
        except:
            return flag

    # def tearDown(self):
    #     self.driver.close()

    if __name__=="__main__":
        unittest.main()
# lc=LoginTestCase()
# lc.test_loginFile()
# aa=lc.getCookie()
# bb=lc.get_token()
# print(aa)
# print(bb)
