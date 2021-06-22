from selenium.webdriver.common.by import By
from basePage import BasePage


class CaseListPage(BasePage):
    # 立案
    file_case = (By.XPATH, "//*[text()='立案']")
    # 回退
    back_case = (By.XPATH, "//*[text()='回退']")
    # 结案
    finish_case = (By.XPATH, "//*[text()='结案']")
    # 问题内容
    question_content = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/ul[3]/li[2]/p/span")


if __name__ == "__main__":
    c = CaseListPage()
    if c.find_ele(c.question_content).text == "测试":
        c.click_element(c.file_case)
