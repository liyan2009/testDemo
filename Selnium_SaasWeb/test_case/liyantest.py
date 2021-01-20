import time
from module.Login import Login
import os
import configparser

from package.browser_engine import BrowserEngine
class TestBrowserEngine(object):
    #URL的地址从配置文件中读取
    def get_value(self):
        dir=os.path.dirname(os.path.abspath('.'))
        config=configparser.ConfigParser()
        fire_path=dir+"/config/config.ini"
        config.read(fire_path)
        url=config.get("testServer","URL")
        return  url
tbe=TestBrowserEngine()
url=tbe.get_value()
l=Login()
mobile="18502038639"
pwd="1234567"
l.login(url,mobile,pwd)