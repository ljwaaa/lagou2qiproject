import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.exercisework.page.basepage import BasePage
from web.exercisework.page.contact_page import Contact


class Importcontact(BasePage):

    def import_contact(self):
        # 导入通讯录点击查看跳转到通讯录界面
        self.find(By.ID, "js_upload_file_input").send_keys(
            r"C:\Users\ljw\PycharmProjects\lagou2q\web\exercisework\通讯录批量导入模板 (1).xlsx")
        self.find(By.ID, "submit_csv").click()
        time.sleep(3)

        # self.driver.find_element_by_link_text("前往查看").click()
        self.find(By.LINK_TEXT, "前往查看").click()
        return Contact()
