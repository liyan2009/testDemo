#! python3
from selenium import webdriver

class Location(object):

    def __init__(self,driver):
        self.driver=driver
    """定义返回"""
    def back(self):
        self.driver.back()
    """定义前进"""
    def forward(self):
        self.driver.forward()
    """封装获取单个元素"""
    def findId(self,id):
        f=self.driver.find_element_by_id(id)
        return f
    def findName(self,name):
        f=self.driver.find_element_by_name(name)
        return f
    def findClassName(self,name):
        f=self.driver.find_element_by_class_name(name)
        return f
    def findTagName(self,name):
        f=self.driver.find_element_by_tag_name(name)
        return f
    def findxpath(self,xpath):
        f=self.driver.find_element_by_xpath(xpath)
        return f
    def findLinkText(self,text):
        f=self.driver.find_element_by_link_text(text)
        return f
    def findpartialLinkText(self,text):
        f=self.driver.find_element_by_partial_link_text(text)
        return f
    def findCss(self,css):
        f=self.driver.find_element_by_css_selector(css)
        return f
    def closeBrowser(self):
        self.driver.quit()
