import time

from selenium.webdriver.common.by import By

from Base.page import Page
from Base.get_driver import get_driver

# 实例化统一入口类
page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

# 点击首页我
page_obj.get_home_page().click_home_my_btn()
# 点击已有账户去登录
page_obj.get_sign_page().click_sign_exits_btn()
# 登录操作
page_obj.get_login_page().login("13488834010", "159357li123")

def get_toast(tos):
    # 获取消息
    xpath_data = (By.XPATH, "//*[contains(@text,'%s')]" % tos)

    toast_text = page_obj.get_setting_page().search_element(xpath_data, timeout=3, poll_frequency=0.5)

    print(toast_text.text)

get_toast("错误")

# # 打印个人中心我的优惠券
# print(page_obj.get_person_page().get_coupons_text())
# # 点击设置按钮
# page_obj.get_person_page().click_setting_btn()
# # 退出登录
# page_obj.get_setting_page().logout('y')


time.sleep(2)
# 退出driver
page_obj.driver.quit()
