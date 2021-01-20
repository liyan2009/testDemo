#! python3
#! -*- coding:utf-8 -*-


from time import sleep

class Page(object):
    #初始化driver,base_url
    def __init__(self,driver,base_url):
        self.driver=driver
        self.base_url=base_url
        print(base_url)

    def find_xpath(self,loc):
        try:
            return self.driver.find_element_by_xpath(loc)
        except:
            print(u"%s 页面未能找到 %s 元素"%(self,loc))

    #通过class进行定位
    def find_class(self,loc):
        try:
            return self.driver.find_element_by_class_name(loc)
        except:
            print(u"%s 页面未能找到 %s 元素"%(self,loc))

    #打开网站
    def open(self,url):
        url=self.base_url+url
        self.driver.get(url)

    #输入值
    def send_keys(self,loc,value,clear_first=True,click_first=True):

            if click_first:
                self.find_xpath(loc).click()
            if clear_first:
                self.find_xpath(loc).clear()
                self.find_xpath(loc).send_keys(value)

    #模拟鼠标点击
    def move_click(self,loc_ele,action):
        sleep(5)
        action.move_to_element(loc_ele).click(loc_ele).perform()



