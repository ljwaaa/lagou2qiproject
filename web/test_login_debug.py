import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_debug_login(self):
        # 实例化option
        option = Options()
        # 指定了调试地址
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)
