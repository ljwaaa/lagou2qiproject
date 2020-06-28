from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.exercisework.page.contact_page import Contact
from web.exercisework.page.import_contact_page import Importcontact
from web.exercisework.page.basepage import BasePage


class IndexPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_import_contact(self):
        # 点击跳转导入通讯录页面
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        return Importcontact()

    def goto_contact(self):
        # 点击跳转联系人界面
        self.find(By.ID, "menu_contacts").click()
        return Contact()
