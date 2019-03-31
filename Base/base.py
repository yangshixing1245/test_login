import time, allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,id属性值) (By.XPATh,xpath属性值) (By.CLSS_NAME,class属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 元素查找间隔时间
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,id属性值) (By.XPATh,xpath属性值) (By.CLSS_NAME,class属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 元素查找间隔时间
        :return: 元素定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=10, poll_frequency=1):
        """
        点击元素
        param loc: 元组 (By.ID,id属性值) (By.XPATh,xpath属性值) (By.CLSS_NAME,class属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 元素查找间隔时间
        :return:
        """
        self.search_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=10, poll_frequency=1):
        """
        输入框输入内容
        :param loc: 元组 (By.ID,id属性值) (By.XPATh,xpath属性值) (By.CLSS_NAME,class属性值)
        :param text: 输入框输入内容
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 元素查找间隔时间
        :return:
        """
        input_text = self.search_element(loc, timeout, poll_frequency)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    def scroll_screen(self, tag):
        """
        滑动屏幕操作
        :param tag: 1:向上滑动 2:向下滑动 3: 向左滑动 4: 向右滑动
        :return:
        """
        import time
        time.sleep(2)
        # 获取屏幕分辨率  {'width', 'height'}
        screen = self.driver.get_window_size()
        # 宽
        width = screen.get("width")
        # 高
        height = screen.get("height")
        # 执行滑动操作  宽 80% 30%   高 80% 30%
        if int(tag) == 1:
            self.driver.swipe(width*0.5, height*0.8, width*0.5, height*0.3, duration=2000)
        if int(tag) == 2:
            self.driver.swipe(width*0.5, height*0.3, width*0.5, height*0.8, duration=2000)
        if int(tag) == 3:
            self.driver.swipe(width*0.8, height*0.5, width*0.3, height*0.5, duration=2000)
        if int(tag) == 4:
            self.driver.swipe(width*0.3, height*0.5, width*0.8, height*0.5, duration=2000)

    def get_toast(self, tos):
        """
        # 获取消息
        :param tos: xpath需要文本
        :return: toast消息文本
        """
        xpath_data = (By.XPATH, "//*[contains(@text,'%s')]" % tos)
        toast_text = self.search_element(xpath_data, timeout=3, poll_frequency=0.5)
        return toast_text.text
    def screen_png(self, name="截图"):
        """添加截图到测试报告"""
        # 定义图片名字
        png_name = "./screen/%d.png" % int(time.time())
        # 截图
        self.driver.get_screenshot_as_file(png_name)
        # 截图添加到测试报告
        with open(png_name, "rb") as f:
            allure.attach(name, f.read(), allure.attach_type.PNG)
