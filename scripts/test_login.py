import sys, os, pytest, allure
sys.path.append(os.getcwd())
from Base.page import Page
from Base.get_driver import get_driver
from Base.getData import GetData
from selenium.common.exceptions import TimeoutException

def get_login_data():
    # [()] 成功数据列表
    suc_list = []  # [(用例编号, 用户名, 密码, 预期结果)]
    # [()]
    fail_list = [] # [(用例编号, 用户名, 密码, toast获取消息, 预期结果)]
    # 读文件数据
    data = GetData().get_read_yml("login_data.yml").get("Login_data")
    for i in data.keys():
        if data.get(i).get("toast_mes"):
            # 预期失败用例添加
            fail_list.append((i, data.get(i).get("username"), data.get(i).get("passwd"),
                              data.get(i).get("toast_mes"), data.get(i).get("exp_data")))
        else:
            # 预期成功用例添加
            suc_list.append((i, data.get(i).get("username"), data.get(i).get("passwd"),
                              data.get(i).get("exp_data")))
    return {"suc": suc_list, "fail": fail_list}

class Test_login:
    def setup_class(self):
        # 声明driver
        self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        # 实例化统一入口类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        # 退出driver
        self.driver.quit()
    @pytest.fixture(autouse=True)
    def in_lobin_page(self):
        """每个方法执行一次"""
        # 点击首页我
        self.page_obj.get_home_page().click_home_my_btn()
        # 点击注册页面已有账号去登录
        self.page_obj.get_sign_page().click_sign_exits_btn()
    @pytest.mark.parametrize("case_num, username, passwd, exp_data", get_login_data().get("suc"))
    def test_suc_login(self, case_num, username, passwd, exp_data):
        """预期成功测试用例"""
        # 登录操作
        self.page_obj.get_login_page().login(username, passwd)
        try:
            # 获取我的优惠券
            coup = self.page_obj.get_person_page().get_coupons_text()
            try:
                assert coup == exp_data
            except AssertionError:
                # 截图 TODO
                self.page_obj.get_login_page().screen_png()
                # 显示断言失败
                assert False
            finally:
                # 点击个人中心设置按钮
                self.page_obj.get_person_page().click_setting_btn()
                # 设置页面执行退出操作
                self.page_obj.get_setting_page().logout('y')
        except TimeoutException:
            # 截图 TODO
            self.page_obj.get_login_page().screen_png()
            """新功能的增加不会选择更改老功能元素属性"""
            # try:
            #     # 执行退出操作
            #     self.page_obj.get_person_page().click_setting_btn()
            #     self.page_obj.get_setting_page().logout('y')
            #
            # except TimeoutException:
            #     # 关闭登录页面--页面还停留在登录页
            #     self.page_obj.get_login_page().close_login_page()
            # 关闭登录页面--页面还停留在登录页
            self.page_obj.get_login_page().close_login_page()
            # 显示断言失败
            assert False
    @pytest.mark.parametrize("case_num, username, passwd, toast_mes, exp_data", get_login_data().get("fail"))
    def test_fail_login(self, case_num, username, passwd, toast_mes, exp_data):
        """预期失败测试用例"""
        # 登录操作
        self.page_obj.get_login_page().login(username, passwd)
        try:
            # 获取toast消息
            message = self.page_obj.get_setting_page().get_toast(toast_mes)
            try:
                # 断言
                assert message == exp_data and self.page_obj.get_login_page().is_login_btn()
            except TimeoutException:
                # 截图 TODO
                self.page_obj.get_login_page().screen_png()
                assert False
            finally:
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()
        except TimeoutException:
            # 截图 TODO
            self.page_obj.get_login_page().screen_png()
            try:
                # 找我的优惠券 ---作为个人中心退出操作
                self.page_obj.get_person_page().get_coupons_text()
                # 点击设置
                self.page_obj.get_person_page().click_setting_btn()
                # 执行退出
                self.page_obj.get_setting_page().logout('y')
            except TimeoutException:
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()
            assert False





