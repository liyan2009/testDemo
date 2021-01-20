#! python3
from selenium import webdriver
from time import sleep

#
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.implicitly_wait(5)
#
# driver.find_element_by_name("wd").send_keys("selenium")
# driver.find_element_by_id("su").click()
# sleep(2)
#
# js="var q=document.documentElement.scrollTop=1000"
# driver.execute_script(js)
# sleep(5)
# driver.quit()
#主要练习父子类继承关系
class Parent(object):
    def dayin(self):
        print("打印父类的方法")
class Child(Parent):
    def dayin(self):
        print("调用父类前的方法")
        super(Child,self).dayin()
        print("调用子类后的方法")



#练习合成的方法
class Foo(object):
    def __init__(self):
        self.other=Parent()

    def dayin(self):
        print("打印前内容")
        self.other.dayin()
        print("调用后的内容")

parent=Parent()
son=Child()

daughter=Foo()
parent.dayin()

print("\n")
son.dayin()

print("\n")
daughter.dayin()

