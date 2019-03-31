from Base.base import Base
from Page.UIElement import UIElement

class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag):
        """
        退出操作
        :param tag: y:确认退出  n:取消退出
        :return:
        """
        # 滑动操作
        self.scroll_screen(1)
        # 点击退出
        self.click_element(UIElement.setting_logout_btn_id)
        if tag == 'y':
            self.click_element(UIElement.setting_logout_acc_btn_id)
        if tag == "n":
            self.click_element(UIElement.setting_logout_dis_btn_id)
