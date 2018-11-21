from Base.Base_Method import Base_Method
import allure
class Operating_Method(Base_Method):
    def __init__(self,driver):
        Base_Method.__init__(self,driver)
    # 获取一组元素的text
    # @allure.step('获取这一组元素的text值')
    def gain_elements_text(self,loc):
        list = []
        elements = self.find_elements(loc)
        for i in elements:
            list.append(i.text)
        return list
    @allure.step('获取textlist')
    def gain_text_list(self,loc):
        s = self.gain_elements_text(loc)
        return allure.attach("列表", "{0}".format(s))
