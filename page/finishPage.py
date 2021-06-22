from basePage import BasePage
from selenium.webdriver.common.by import By


class FinishPage(BasePage):
    # 待结案
    wait_finish_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[2]")
    # 案件采集来源其他及上级工单编号
    test_case_num = (By.XPATH, "//tr/td[text()='其他']/preceding-sibling::td[1][text()='—']")
    # 页数
    page_count = (By.XPATH, "//li[@tabindex='0']")
    # 驳回
    overruled = (By.XPATH, "//*[text()='驳回']/..")
    # 结案
    finished = (By.XPATH, "//*[text()='结案']/..")
    # 案件问题内容
    case_question_content = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/ul[3]/li[2]/p/span")
    # 结案意见
    finished_opining = (By.XPATH, "//p[text()='结案意见：']/following-sibling::div[1]/textarea")
    # 取消
    cancel = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div/div[1]/div[4]/div[8]/button/div/div[2]/div[1]")
    # 确定
    sure = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div/div[1]/div[4]/div[8]/button/div/div[2]/div[2]")
    # 回访
    return_visit = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div/div[1]/div[4]/div[8]/button/div/div[2]/div[3]")
    # 未填写结案意见提示框
    tips = (By.XPATH, "//span[text()='结案意见尚未全部填写']")


if __name__ == "__main__":
    f = FinishPage()
    page = f.find_eles(f.page_count)[:-1]
    for page_num in (2, len(page) + 1):
        if f.find_element(f.test_case_num) is None:
            print("第%d页,没有找到内容" % (page_num-1))
            f.find_element(f.page_count[page_num]).click()
        else:
            f.find_element(f.test_case_num).click()
            break

