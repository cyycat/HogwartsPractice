from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.common.by import By


class TestTouchActions:
    """
    搜索，并滑动到搜索结果页底部
    """

    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch_action_scrollbottom(self):
        """
        1 打开Chrome
        2 打开 https://baidu.com/
        3 向搜索框输入"selenium测试"
        4 通过 TouchAction 点击搜索框
        5 滑动到底部，点击下一页
        6 关闭Chrome
        :return:
        """
        self.driver.get("https://baidu.com/")
        ele = self.driver.find_element(By.XPATH, '//*[@id="form"]/span[1]')
        ele_search = self.driver.find_element_by_id("su")
        ele.send_keys(["selenium测试"])

        action = TouchActions(self.driver)
        # 点击搜索
        action.tap(ele_search)
        action.perform()
        sleep(3)

        # 滑动到底部
        action.scroll_from_element(ele, 0, 10000)
        action.perform()
        sleep(3)