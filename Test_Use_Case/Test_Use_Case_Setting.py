from Base.Get_Driver import Get_Driver
from Page.Return_Page import Return_Page
import Page,allure,pytest,time,sys,os
from Yaml.read_yaml import Read_Data
sys.path.append(os.getcwd())

def yaml():
    list_data = []
    yaml_data = Read_Data('search_data.yaml').return_data()
    for i in yaml_data.keys():
        list_data.append((i,yaml_data.get(i).get('user'),yaml_data.get(i).get('password'),yaml_data.get(i).get('tag')))
    return list_data

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
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=1)
    @allure.step('爱优品二手手机登录功能的正确性验证')
    @pytest.mark.parametrize('test_id,user,password,tag',yaml())
    def test_love_register(self,test_id,user,password,tag):
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
        time.sleep(1)
        self.Dv.return_page().send_keys_text(Page.user_input,user)
        self.Dv.return_page().send_keys_text(Page.password_input,password)
        # 点击确定按钮
        self.Dv.return_page().click_confirm_button()
        time.sleep(1)
        if tag:
            try:
                self.Dv.return_page().gain_text_list(Page.my_list_text)
            except EnvironmentError:
                pass
            finally:
                # 点击回退按钮
                self.Dv.return_page().click_back_button()
        else:
            time.sleep(1)
            # 屏幕向上滑动
            self.Dv.return_page().slide_up()
            # 点击退出当前账号按钮
            self.Dv.return_page().click_quit_button()
            # 点击确定退出弹窗确定按钮
            self.Dv.return_page().click_config_quit_button()
