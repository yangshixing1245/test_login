from Base.base import Base
from Page.UIElement import UIElement


class PersonPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_coupons_text(self):
        """获取我的优惠券文本"""
        # 定位优惠券
        coupons_text = self.search_element(UIElement.person_coupons_id).text
        return coupons_text

    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_element(UIElement.person_setting_btn)
