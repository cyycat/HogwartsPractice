
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")

    def teardown(self):
        self.driver.quit()


    def test_wait_display(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()

        # 显示等待

        # 步骤一：自定义函数wait一定要写一个入参，因为源码中until调用wait时，会传入一个参数
        def wait(x):
            return len(self.driver.find_elements(By.LINK_TEXT, "求职面试圈")) >= 1

        # 步骤二：循环调用wait函数，直至return True, 若超过超时时间10秒，则报异常TimeoutException
        WebDriverWait(self.driver, 10).until(wait)

        self.driver.find_element(By.LINK_TEXT, "求职面试圈").click()
