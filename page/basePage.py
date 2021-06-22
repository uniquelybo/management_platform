from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        print("------------")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "D:\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        self.wait = WebDriverWait(self.driver, 5, 0.5)
        print(self.driver.title)

    # 查找元素
    def find_element(self, ele_loc):
        print(ele_loc)
        try:
            ele = self.wait.until(lambda driver: self.driver.find_element(*ele_loc))
            print(ele)
            return ele
        except Exception as e:
            print("元素查找错误---", e)
            return

    def find_eles(self, ele_loc):
        return self.driver.find_elements(*ele_loc)

    def find_ele(self, ele_loc):
        return self.find_element(*ele_loc)

    # 文本元素输入内容
    def element_input_text(self, ele_loc, text):
        print(ele_loc, text)
        self.find_element(*ele_loc).send_keys(text)

    # 文本元素清空内容
    def element_clear_text(self, ele_loc):
        self.find_element(*ele_loc).clear()

    # 点击元素
    def click_element(self, ele_loc):
        ele = self.find_element(*ele_loc)
        ele.click()

    # 清除cookies
    def clear_cookies(self):
        self.driver.delete_all_cookies()

    # 刷新页面
    def refresh_web(self):
        self.driver.refresh()
