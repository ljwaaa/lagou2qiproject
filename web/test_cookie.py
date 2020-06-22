import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testcookie():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.maximize_window()

    def test_get_cookie(self):

        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 添加一个dic信息,把cookie键值对一个一个塞入浏览器中
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            lens = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if lens is not None:
                break

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(
            r"C:\Users\ljw\PycharmProjects\yanshi\test_selenium\ljw.xls")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "upload_file_name")))
        ele = self.driver.find_element(By.ID, "upload_file_name").text
        assert ele == "ljw.xls"

    def teardown(self):
        self.driver.quit()
