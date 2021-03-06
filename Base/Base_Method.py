from selenium.webdriver.support.wait import WebDriverWait
import allure,Page

class Base_Method:
    # 初始化driver
    def __init__(self,driver):
        self.driver = driver
    # 定位单个元素
    def find_element(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    # 定位一组元素
    def find_elements(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    # 点击
    def click_element(self,loc):
        self.find_element(loc).click()
    # 输入
    @allure.step('输入操作')
    def send_keys_text(self,loc,text):
        element = self.find_element(loc)
        element.clear()
        element.send_keys(text)
        allure.attach('输入','{0}'.format(text))