#! python3
#-*- coding:utf-8 -*-

from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver


class BasePage(object):
    def __init__(self,browser='Chrome'):
        if browser=='firefox' or browser=='ff':
            driver=webdriver.Firefox()
        elif browser=='Chrome':
            driver=webdriver.Chrome()
        elif browser=='IE':
            driver=webdriver.Ie()
        try:
            self.driver=driver
        except Exception:
            raise NameError("Not found %s browser,IE"% browser)

    #查找单一元素
    def findElement(self,element):
        try:
            type = element[0]
            value = element[1]
            if type=="id" or type=='ID' or type=='Id':
                elem=self.driver.find_element_by_id(value)
            elif type=="name" or type=="Name" or type=="NAME":
                elem=self.driver.find_element_by_name(value)
            elif type=="xpath" or type=="Xpth" or type=="XPTH":
                elem=self.driver.find_elements_by_xpath(value)
            elif type == "class" or type == "Class" or type == "CLASS":
                elem=self.driver.find_element_by_class_name(value)
            elif type == "css" or type == "Css" or type == "CSS":
                elem=self.driver.find_element_by_css_selector(value)
            elif type == "link_text" or type == "Link_text" or type == "LINK_TEXT":
                elem=self.driver.find_elements_by_link_text(value)
            elif type == "tag" or type == "Tag" or type == "TAG":
                elem=self.driver.find_element_by_tag_name(value)
            else:
                raise ValueError("请选择请求的函数类型")
        except Exception:
            raise ValueError("Not found %s element"+str(element))
        return elem

    #查找多个元素
    def findElements(self,element):
        try:
            type = element[0]
            value = element[1]
            if type=="id" or type=='ID' or type=='Id':
                elems=self.driver.find_elements_by_id(value)
            elif type=="name" or type=="Name" or type=="NAME":
                elems=self.driver.find_elements_by_name(value)
            elif type=="xpath" or type=="Xpth" or type=="XPTH":
                elems=self.driver.find_elements_by_xpath(value)
            elif type == "class" or type == "Class" or type == "CLASS":
                elems=self.driver.find_elements_by_class_name(value)
            elif type == "css" or type == "Css" or type == "CSS":
                elems=self.driver.find_elements_by_css_selector(value)
            elif type == "link_text" or type == "Link_text" or type == "LINK_TEXT":
                elems=self.driver.find_elements_by_link_text(value)
            elif type == "tag" or type == "Tag" or type == "TAG":
                elems=self.driver.find_elements_by_tag_name(value)
            else:
                raise ValueError("请选择请求的函数类型")
        except Exception:
            raise ValueError("Not found %s element"+str(element))
        return elems

    #打开网址
    def open(self,url):
        if url!="":
            self.driver.get(url)
        else:
            raise ValueError("请输入正确的url")

    #获取标题
    def getTitle(self):
        return self.driver.title

    #获取元素的Text值
    def getText(self,element):
        return element.text

    #点击元素
    def click(self,element):
        element.click()

    #退出
    def quit(self):
        self.driver.quit()

    #往前
    def forward(self):
        self.driver.forward()

    #往后
    def back(self):
        self.driver.back()

    #给元素赋值
    def setText(self,element,text):
        element.send_keys(text)

    #给元素赋值
    def enter(self,element):
        element.send_keys(Keys.RETURN)

    #窗口最大化
    def maximizeWindow(self):
        self.driver.maximize_window()
