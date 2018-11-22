from appium.webdriver.common.touch_action import TouchAction
from Base.Base_Method import Base_Method
import allure,Page

class Operating_Method(Base_Method):
    def __init__(self,driver):
        Base_Method.__init__(self,driver)
    # 点击进入爱优品按钮
    def click_love_button(self):
        self.click_element(Page.login_love_button)
    # 点击始终允许按钮
    def click_all_allow_button(self):
        self.click_element(Page.all_allow_button)
    # 点击我的按钮
    def click_my_button(self):
        self.click_element(Page.my_button)
    # 点击马上登录按钮
    def click_atonce_rgisrer_button(self):
        self.click_element(Page.atonce_register_button)
    # 点击确定按钮
    def click_confirm_button(self):
        self.click_element(Page.confirm_button)
    # 点击退出当前账号按钮
    def click_quit_button(self):
        self.click_element(Page.quit_button)
    # 点击确定退出弹窗中确定按钮
    def click_config_quit_button(self):
        self.click_element(Page.confiem_quit_button)
    # 点击取消更新按钮
    def click_update_cancle_button(self):
        self.click_element(Page.update_cancel_button)
    # 获取一组元素的text
    def gain_elements_text(self,loc):
        list = []
        elements = self.find_elements(loc)
        for i in elements:
            list.append(i.text)
        return list
    @allure.step('gain_text_list')
    def gain_text_list(self,loc):
        s = self.gain_elements_text(loc)
        return allure.attach('list', "{0}".format(s))
    @allure.step('页面向右滑动')
    def slide_right(self):
        TouchAction(self.driver).press(x=952,y=1007).move_to(x=14,y=984).release().perform()
    @allure.step('页面向上滑动')
    def slide_up(self):
        TouchAction(self.driver).press(x=466,y=1698).move_to(x=489,y=118).release().perform()
    @allure.step('页面向下滑动')
    def slide_below(self):
        TouchAction(self.driver).press(x=489,y=118).move_to(x=466,y=1698).release().perform()