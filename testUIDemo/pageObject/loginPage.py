#! python3
#! -*- coding:utf-8 -*-

from pageObject.page import Page
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class LoginPage(Page):

    username_loc="//input[@formcontrolname='mobile']"   #手机号
    pwd_loc="//input[@formcontrolname='password']" #密码
    btn_loc="//form/button" #按钮
    wx_loc="//div[@class='login-box']/div[@class='box']/ul[@class='tabs clearfix']/li[2]/div" #登录页面切换到用户名密码界面
    url="https://i.mayitest.cn/"

    user_error="//form/div[1]/div/span" #错误的用户名
    pwd_error="//form/div[2]/div/span" #错误的密码

    #输入用户名
    def input_username(self, username):
        self.find_xpath(self.username_loc).send_keys(username)

    #输入密码
    def input_pwd(self, pwd):
        self.find_xpath(self.pwd_loc).send_keys(pwd)

    #点击按钮
    def click_btn(self):
        self.find_xpath(self.btn_loc).click()

    #点击页签 微信登录
    def click_wx(self,action):
        self.open(self.url)
        wx_ele=self.find_xpath(self.wx_loc)
        self.move_click(wx_ele,action)
        sleep(2)

    #登录成功 ,usename,pwd
    def user_login(self,usename,pwd):
        self.input_username(usename)
        self.input_pwd(pwd)
        self.click_btn()
        sleep(2)

    #用户名错误
    def login_error_user(self):
        return  self.find_xpath(self.user_error).text

    #密码错误
    def login_error_pwd(self):
        return  self.find_xpath(self.pwd_error).text

# driver=webdriver.Chrome()
# url="https://i.mayitest.cn/"
#
# lp=LoginPage(driver,url)
# action=ActionChains(driver)
# lp.click_wx(action)
#
# lp.user_login("","")
# print(lp.login_error_user())
# print(lp.login_error_pwd())



