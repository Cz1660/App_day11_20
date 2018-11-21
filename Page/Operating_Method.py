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

    @allure.step('获取这一组元素的text值')
    def gain_list(self,loc):
        list = self.gain_elements_text(loc)
        allure.attach('描述',list)
