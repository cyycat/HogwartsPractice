
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")

        # 隐式等待 3秒
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait_implicitly(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        self.driver.find_element(By.LINK_TEXT, "求职面试圈").click()