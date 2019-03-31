from Base.base import Base
from Page.UIElement import UIElement


class SignPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_sign_exits_btn(self):
        """点击已有账号去登录"""
        self.click_element(UIElement.sign_exits_account_id)

