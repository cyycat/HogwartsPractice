
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 测试用例的关键要素
# 导入依赖
# 创建driver
# 执行自动化步骤
# 断言

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://testerhome.com/")

class TestHogwarts:
    def setup(self):
        # 如果本地环境变量没有配置driver,就需要把driver下载后，把路径放入executable_path中
        # self.driver = webdriver.Chrome(executable_path="driver详细路径")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待：打开新页面时，动态等待5秒，如果在第1秒找到这个元素就继续往下执行，如果没找到就等待，直到5秒后还没找到，就会抛出异常
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        self.driver.find_element(By.LINK_TEXT, "求职面试圈").click()
        sleep(2)


