#! python3
#-*- coding:utf-8 -*-

from WebPages.BasePage import BasePage
import time

class LoginPage(BasePage):

    inputbox=("tag","input")
    button=("tag","button")

    def __init__(self,browser='Chrome'):
        super().__init__(browser)

    #测试登录
    def login(self,username,pwd):
        inputBox=self.findElements(self.inputbox)
        self.setText(inputBox[0],username)
        self.setText(inputBox[1], pwd)
        time.sleep(2)
        loginButton=self.findElement(self.button)
        loginButton.click()

    #比较结果
    def compareResult(self,expertResult):
        pass
