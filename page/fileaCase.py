import time

from basePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class FileCase(BasePage):
    # 待立案案件
    wait_file_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[1]")
    # 待结案
    wait_finish_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[2]")
    # 回退案件
    back_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[4]")
    # 内容搜索
    content_search = (By.XPATH, "//*[text()='内容搜索']/../following-sibling::div[1]//input")
    # 问题来源
    source_question = (By.XPATH, "//*[text()='问题来源']/../following-sibling::div[1]//span")
    # 所属区域
    same_area1 = (By.XPATH, "//*[text()='所属区域']/../following-sibling::div[1]//span")
    same_area2 = (By.XPATH, "//*[text()='所属区域']/../../following-sibling::div[1]//span")
    # 一类类型
    one_type = (By.XPATH, "//*[text()='一类类型']/../following-sibling::div[1]//span")
    # 案件日期
    case_time = (By.XPATH, "//*[text()='案件日期']/../following-sibling::div[1]")
    # start_time = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div/input")
    # start_time = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[1]/form/div[6]/div[2]/div/span/span/span/input[1]")
    end_time = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/input")

    # 搜索
    search_button = (By.XPATH, "//*[text()=' 搜索 ']")

    # 采集来源其他案件
    chooice_case = (By.XPATH, "//tr/td[text()='其他']")

    # 选择值
    def chooice_value(self, value):
        value = (By.XPATH, "//*[@role='listbox']/li[text()=' %s ']" % value)
        self.click_element(value)


if __name__ == "__main__":
    f = FileCase()
    # print(time.strftime("%Y/%m/%d %H/%M/%S", (2021, 5, 19, 0, 0, 0, 0, 0, 0)))
    # print(time.strftime("%Y/%m/%d %H/%M/%S", (2021, 5, 20, 0, 0, 0, 0, 0, 0)))
    # # f.click_element(f.case_time)
    # f.element_input_text(f.start_time, time.strftime("%Y/%m/%d %H/%M/%S", (2021, 5, 19, 0, 0, 0, 0, 0, 0)))
    # f.element_input_text(f.end_time, time.strftime("%Y/%m/%d %H/%M/%S", (2021, 5, 20, 0, 0, 0, 0, 0, 0)))
    # f.click_element(f.chooice_case)

    # print(f.question_content)
    # content = f.find_element(f.question_content).text
    # print(content=="技术人员测试案件，请撤销办理至公共栏")

    f.click_element(f.wait_file_case)
    f.click_element(f.chooice_case)
