#! python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from module.uploadFile import UpLoadFile
from module.login import LoginTestCase
import unittest

class UploadYuan(object):

    def __init__(self):
        self.ln=LoginTestCase()
        self.driver=self.ln.test_loginFile()
        # aa=self.ln.getCookie()

    #上传员工
    def test_upload(self):
        mydriver=self.driver
        print(mydriver.get_cookie("mayihr_token"))
        sleep(2)
        ele=mydriver.find_element_by_xpath("//div[@class='modal-dialog']/div[@class='footer']/span")
        sleep(3)
        print("bbbbbbdk的福晶科技贷款给")
        ele.click()
        #如果出现广告窗口就关闭
        element="app-dashboard > app-notice-m > div > div.modal-dialog > div.modal-footer.b-t.t-r.pointer.clearfix.lh-60.p-r-lg.pos-a > div"
        flag=self.ln.isElementExist(element)
        print(flag)
        if flag:
            tz_window=mydriver.find_element_by_css_selector(element)
            tz_window.click()
        print("我要测试")
        #点击员工名录
        sleep(2)
        yg_menu=mydriver.find_element_by_css_selector("app-router-sidebar > div > ul > li:nth-child(2) > a > div")
        yg_menu.click()


        #点击批量上传员工
        sleep(2)
        pl_button=mydriver.find_element_by_css_selector("app-staff-list > div > div.clearfix.b-t > div > a.p-l-lg.pointer-blue > span")
        pl_button.click()
        print("aaaaa")
        #点击上传文件
        sleep(2)
        load_btn=mydriver.find_element_by_css_selector(" app-staff-batch-upload > div > div.t-c.clearfix.m-t > div.pos-r.d-ib.m-t-xl > p").click()
        # send_keys("D:\\autoAPI\fileName.xls")
        sleep(2)
        filePath="D:\\autoAPI\\fileName.xls"
        UpLoadFile.upload(filePath)

uy=UploadYuan()
uy.test_upload()