import time

from basePage import BasePage
from selenium.webdriver.common.by import By


class AuditCasePage(BasePage):
    # 待审核案件
    wait_audit_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[2]")
    # 案件采集来源其他及上级工单编号
    test_case_num = (By.XPATH, "//tr/td[text()='其他']/preceding-sibling::td[1]")
    # 案件问题内容
    case_question_content = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/ul[3]/li[2]/p/span")
    # 审核
    case_audit = (By.XPATH, "//*[text()='审核']/..")
    # 转派
    case_turn_dispatch = (By.XPATH, "//*[text()='转派']/..")
    # 上报人信息
    user_data = (By.XPATH, "//*[text()='是否显示上报人信息']")
    # 是否保密
    secret_value = (By.XPATH, "//*[text()='是否保密：']/span")
    # 上报人姓名
    user_name = (By.XPATH, "//*[text()='上报人姓名：']/span")
    # 手机号
    user_phone = (By.XPATH, "//*[text()='手机号：']/span")
    # 性别
    user_sex = (By.XPATH, "//*[text()='性别：']/span")
    # 审核状态
    audit_state = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div/div[1]/div[4]/div[3]/button/div/div[1]/span/div[2]/ul/div/div/li/div[2]/div[1]/div/div")
    # 通过
    audit_pass = (By.XPATH, "//ul[@role='listbox']/li[text()=' 通过 ']")
    # 驳回
    audit_reject = (By.XPATH, "//ul[@role='listbox']/li[text()=' 驳回 ']")
    # 审核意见
    audit_opining = (By.XPATH, "//*[text()='状态：']/../following-sibling::div[1]//textarea")
    # 确定
    audit_sure = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div/div[1]/div[4]/div[3]/button/div/div[2]/div[2]")
    # 取消
    audit_cancel = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div/div[1]/div[4]/div[3]/button/div/div[2]/div[1]")


if __name__ == "__main__":
    a = AuditCasePage()
    # if a.find_ele(a.test_case_num).text == "—":
    #     a.click_element(a.test_case_num)
    #     a.click_element(a.case_audit)
    #     time.sleep(0.5)
    #     a.click_element(a.user_data)
    a.click_element(a.audit_state)
    # a.click_element(a.audit_reject)
    a.element_input_text(a.audit_opining, "测试")
