from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class TestActionChains:
    """
    1 点击/双击/右键
    2 移动光标
    3 拖拽
    4 模拟按键
    """

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 点击/双击/右键
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        element_double_click = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        element_right_click = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')

        action = ActionChains(self.driver)
        # 点击
        action.click(element_click)
        # 右键点击
        action.context_click(element_right_click)
        # 双击
        action.double_click(element_double_click)
        action.perform()

        sleep(3)

    # 移动光标
    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')

        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

        sleep(3)

    # 拖拽
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_source = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
        ele_target = self.driver.find_element(By.XPATH, '//*[@class="item"][3]')

        action = ActionChains(self.driver)
        action.drag_and_drop(ele_source, ele_target)
        # 下面2种写法效果一致
        # action.click_and_hold(ele_source).release(ele_target)
        # action.click_and_hold(ele_source).move_to_element(ele_target).release()
        action.perform()

        sleep(3)


    # 模拟按键
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.CSS_SELECTOR, 'body > label:nth-child(2) > input[type="textbox"]')
        ele.click()

        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()

        sleep(3)





