from web.exercisework.page.index_page import IndexPage


class Testimportcontact():
    def test_import(self):
        index = IndexPage()
        # 1.点击导入通讯录2.上传文件3.点击确认导入4.点击前往查看5.添加断言
        assert "张三（示例）" in index.goto_import_contact().import_contact().getmember()
