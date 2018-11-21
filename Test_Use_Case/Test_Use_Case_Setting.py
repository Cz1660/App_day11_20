from Base.Get_Driver import Get_Driver
from Page.Return_Page import Return_Page
import Page,allure
class Test_Login:
    def setup_class(self):
        self.Dv = Return_Page(Get_Driver().get_driver())
    def teardown_class(self):
        self.Dv.driver.quit()
    def test_setting(self):
        for i in Page.input_list:
            self.Dv.return_page().send_keys_text(Page.search_setting,i)