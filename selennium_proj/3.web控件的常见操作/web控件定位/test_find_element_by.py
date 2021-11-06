from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestXpath:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def test_find_element(self):
        # 1、输入框输入文字"霍格沃兹测试学院"

        # 以下4种方式，效果相同
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys("霍格沃兹测试学院")

        # 2、点击搜索
        self.driver.find_element(By.CSS_SELECTOR, '[id="su"]').click()
        sleep(2)


    def teardown(self):
        self.driver.quit()
