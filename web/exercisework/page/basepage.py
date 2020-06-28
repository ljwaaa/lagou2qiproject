from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    # 定义一个url属性初始为空，通过主界面覆盖来传值
    base_url = ""

    # 初始化方法，浏览器复用调试
    def __init__(self, driver_basepage: WebDriver = None):
        if driver_basepage == None:

            option = Options()
            # 指定了调试地址
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)

        else:
            self.driver = driver_basepage
        if self.base_url != "":
            self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)

    # 封装了查找单个元素定位方式
    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    # 封装了查找多个元素定位方式
    def finds(self, by, value):
        return self.driver.find_elements(by=by, value=value)

    def waitlimit(self, time, by, value):
        WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located((by, value)))
