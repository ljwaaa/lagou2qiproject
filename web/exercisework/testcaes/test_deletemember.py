import time

from selenium.webdriver.common.by import By

from web.exercisework.page.basepage import BasePage
from web.exercisework.page.index_page import IndexPage


class Testdeletemember():
    def test_delete(self):
        index = IndexPage()
        # 1.点击所要删除的联系人2.点击删除3.添加断言

        index.goto_contact().deletemember()
        wait = BasePage()
        wait.waitlimit(10, By.CSS_SELECTOR, ".js_member_count")

        member_lists = index.goto_contact().getmember()

        assert "张三（示例）" not in member_lists
