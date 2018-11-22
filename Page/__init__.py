from selenium.webdriver.common.by import By

# 设置
search_setting = (By.ID,'android:id/search_src_text')
search_result = (By.ID,'com.android.settings:id/title')
input_list = ['移动网络','电池']

# 爱优品二手手机
login_love_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/ip_ll_enter')
all_allow_button = (By.ID,'com.android.packageinstaller:id/permission_allow_button')
update_cancel_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/dc_left')
my_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_tv_my')
my_list_text = (By.CLASS_NAME,'android.widget.TextView')
atonce_register_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_civ_header')
user_input = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_user')
password_input = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_pwd')
confirm_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_ll_login')
quit_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_ll_out_login')
confiem_quit_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/dc_right')

assert_text = ['马上登录']
input_user_password = [['13198690728','aaa123456'],[' 13198690728','aaa123456'],['13198690728 ','aaa123456'],
                       ['13198690728',' aaa123456'],['13198690728','aaa123456 '],['131986907288','aaa123456',1]]
