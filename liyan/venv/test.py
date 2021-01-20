#coding=utf-8
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
'''driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.set_window_size(500,600)
driver.close()
'''
def openBaidu():
    dr=webdriver.Chrome()
    dr.get("http://www.baidu.com")
    dr.find_element_by_id("kw").send_keys("selenium")
    dr.find_element_by_id("su").click()
    sleep(3)
    dr.back()
    sleep(2)
    dr.close()

def login(username,password):
    driver=webdriver.Chrome()
    sleep(2)
    driver.get("https://www.mayitest.cn/#/entry/login")
    #进行右键操作
    #mobile=driver.find_element_by_css_selector('input[formcontrolname="mobile"]')
    #ActionChains(driver).context_click(mobile).perform()
    #driver.find_element_by_xpath('//input[@formcontrolname="mobile"]').send_keys(username)
    driver.find_element_by_css_selector('input[formcontrolname="mobile"]').send_keys(username)
    driver.find_element_by_css_selector('input[formcontrolname="password"]').send_keys(password)
    #driver.find_element_by_xpath('//input[@formcontrolname="password"]').send_keys(password)
    #这种方式也是可以的
    #driver.find_element_by_xpath('//button[contains(text(),"登录")]').click()
    driver.find_element_by_css_selector("[class='btn v-m btn-sm w-100']").click()
    sleep(2)
    title=driver.title
    if(title=="首页"):
        print("success")
    else:
        print("fail")

login("18502038639","1234567")
