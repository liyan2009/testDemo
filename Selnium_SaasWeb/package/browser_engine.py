#! python3
from selenium import webdriver

"""定义一个浏览器引擎类"""
class BrowserEngine(object):
    browser_type = "Chrome"

    def get_browser(self):
        """通过if语句来控制初始化不同的浏览器"""
        if self.browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif self.browser_type == 'IE':
            driver = webdriver.Ie()
        elif self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        #driver.maximize_window()
        return driver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")