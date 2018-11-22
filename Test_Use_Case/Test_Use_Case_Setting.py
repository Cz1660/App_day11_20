from Base.Get_Driver import Get_Driver
from Page.Return_Page import Return_Page
import Page,allure,pytest,time
# class Test_Login_Setting:
#     def setup_class(self):
#         self.Dv = Return_Page(Get_Driver().get_driver('com.android.settings','.HWSettings'))
#     def teardown_class(self):
#         self.Dv.driver.quit()
#     @pytest.mark.run(order=1)
#     @allure.step('搜索设置输入框的正确性验证')
#     def test_setting(self):
#         # 输入并断言
#         for i in Page.input_list:
#             self.Dv.return_page().send_keys_text(Page.search_setting,i)
#             self.Dv.return_page().gain_text_list(Page.search_result)
#             assert i in self.Dv.return_page().gain_elements_text(Page.search_result)

class Test_Login_Love_Regiter:
    def setup_class(self):
        self.Dv = Return_Page(Get_Driver().get_driver
                              ('com.huashidai.cl.lovegoods.lovegoods', '.activity.home.PageActivity'))
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=2)
    @allure.step('爱优品二手手机登录功能的正确性验证')
    def test_love_register(self):
        # 屏幕向右滑动3次
        for i in range(3):
            self.Dv.return_page().slide_right()
        # 点击进入爱优品按钮
        self.Dv.return_page().click_love_button()
        time.sleep(1)
        # 点击取消更新按钮
        self.Dv.return_page().click_update_cancle_button()
        # 屏幕向上滑动
        self.Dv.return_page().slide_up()
        # # 点击始终允许按钮
        # self.Dv.return_page().click_all_allow_button()
        # 点击我的按钮
        self.Dv.return_page().click_my_button()
        # 断言是否是未登录状态
        try:
            assert Page.assert_text[0] in self.Dv.return_page().gain_elements_text(Page.my_list_text)
        except Exception as E:
            allure.attach('error','{0}'.format(E))
        finally:
            self.Dv.return_page().click_my_button()
        # 点击马上登录按钮
        self.Dv.return_page().click_atonce_rgisrer_button()
        # 输入账号密码
        for i in Page.input_user_password:
                self.Dv.return_page().send_keys_text(Page.user_input,i[0])
                self.Dv.return_page().send_keys_text(Page.password_input,i[1])
                # 点击确定按钮
                self.Dv.return_page().click_confirm_button()
                time.sleep(1)
                self.Dv.return_page().gain_text_list()
                if len(i) == 2:
                    time.sleep(1)
                    # 屏幕向上滑动
                    self.Dv.return_page().slide_up()
                    # 点击退出当前账号按钮
                    self.Dv.return_page().click_quit_button()
                    # 点击确定退出弹窗确定按钮
                    self.Dv.return_page().click_config_quit_button()
                    time.sleep(1)
                    # 点击马上登录按钮
                    self.Dv.return_page().click_atonce_rgisrer_button()
                else:
                    # 断言是否定位到我的按钮
                    try:
                        assert self.Dv.return_page().find_element(Page.my_button)
                    except Exception as E:
                        allure.attach('error', '{0}'.format(E))
                    finally:
                        allure.attach('error', '{0}'.format('未定位到我的按钮，登录失败！'))