from Base.Get_Driver import Get_Driver
from Page.Return_Page import Return_Page
import Page,allure,pytest
class Test_Login:
    def setup_class(self):
        self.Dv = Return_Page(Get_Driver().get_driver())
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=1)
    @allure.step('搜索设置输入框的正确性验证')
    def test_setting(self):
        for i in Page.input_list:
            self.Dv.return_page().send_keys_text(Page.search_setting,i)
            assert '无线和网络'or '电池' in self.Dv.return_page().gain_elements_text(Page.search_result)

