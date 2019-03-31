from Base.base import Base
from Page.UIElement import UIElement


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, username, password):
        """
        登录操作
        :param username: 登录用户名
        :param password: 登录密码
        :return:
        """
        # 输入用户名
        self.send_element(UIElement.login_account_id, username)
        # 输入密码
        self.send_element(UIElement.login_passwd_id, password)
        # 点击登录按钮
        self.click_element(UIElement.login_btn_id)

    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(UIElement.login_close_page_id)

    def is_login_btn(self):
        """判断登录按钮是否存在， 存在返回True 不存在返回False"""
        try:
            self.search_element(UIElement.login_btn_id)
            return True
        except:
            return False

