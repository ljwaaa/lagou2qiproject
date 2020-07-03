import time

import pytest
import yaml
from appium import webdriver


class Testdemo:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = ' com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//* [@text='通讯录']").click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,sex,number', yaml.safe_load(open("./wechat_data.yml", encoding='utf-8'), ))
    def test_addcontact(self, name, sex, number):
        sexname = sex

        self.driver.find_element_by_xpath("//* [@text='添加成员']").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("手动输入添加")').click()
        self.driver.find_element_by_xpath("//* [@text='必填']").send_keys(name)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("男")').click()
        if sexname == sex:
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        self.driver.find_element_by_xpath("//*[@text='手机号']").send_keys(number)
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        assert self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text == '添加成功'
        self.driver.back()

    @pytest.mark.parametrize('name,sex,number', yaml.safe_load(open("./wechat_data.yml", encoding='utf-8'), ))
    def test_deletecontact(self, name, sex, number):

        self.driver.find_element_by_id("com.tencent.wework:id/h9u").click()
        self.driver.find_element_by_xpath(f"//* [@text='{name}']").click()
        self.driver.find_element_by_xpath("//*[@text='删除成员']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        time.sleep(2)

        memberlist = self.driver.find_elements_by_xpath(
            "//* [@resource-id='com.tencent.wework:id/dec' ] //* [@class='android.widget.TextView']")

        number = [i.get_attribute("text") for i in memberlist]
        assert name not in number
        self.driver.back()
