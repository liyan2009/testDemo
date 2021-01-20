#! python3
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from package.browser_engine import BrowserEngine
from package.loactaion import Location
from package.browser_engine import BrowserEngine

class Login(object):
    be=BrowserEngine()
    global driver
    driver = be.get_browser()
    def login(self,url,mobile,pwd):
        global  driver
        driver.get(url)
        loc=Location(driver)
        loc.findCss("input[formcontrolname='mobile']").send_keys(mobile)
        driver.implicitly_wait(2)
        loc.findCss("input[formcontrolname='password']").send_keys(pwd)
        driver.implicitly_wait(2)
        loc.findCss("button[class='btn v-m btn-sm w-100']").click()
        time.sleep(5)








