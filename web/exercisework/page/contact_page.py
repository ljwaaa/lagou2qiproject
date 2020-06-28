from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.exercisework.page.basepage import BasePage


class Contact(BasePage):

    def getmember(self):
        # 获取所有的联系人
        self.member_list = []
        member = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # for common in member:
        #     member_list.append(common.get_attribute("title"))
        # 换种列表推导式方式来写
        member_list = [common.get_attribute("title") for common in member]

        return member_list

    def deletemember(self):
        # 删除联系人,点击确认还是返回此界面
        self.find(By.CSS_SELECTOR, ".js_unsortable.js_list.ui-sortable tr:nth-child(1) input").click()
        self.find(By.CSS_SELECTOR, ".js_delete").click()

        # self.driver.find_element_by_xpath("//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
        self.find(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
