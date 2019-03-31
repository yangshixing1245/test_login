from Base.base import Base
from Page.UIElement import UIElement

class HomePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_home_my_btn(self):
        """点击首页我的按钮"""
        self.click_element(UIElement.home_my_btn_id)

