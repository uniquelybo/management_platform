from basePage import BasePage
from selenium.webdriver.common.by import By


class SecondHandleCasePage(BasePage):
    # 待处理案件
    wait_handle_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[1]")
    # 案件信息其他来源
    source_information_case = (By.XPATH, "//tr/td[text()='其他']")
    # 案件问题内容
    case_question_content = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div/div[3]/div/div[1]/div[2]/div[2]/ul[3]/li[2]/p/span")
    # 转派
    turn_dispatch = (By.XPATH, "//*[text()=' 转派 ']")
    # 处置
    handle = (By.XPATH, "//*[text()=' 处置 ']")
    # 处置意见
    handle_opining = (By.XPATH, "//*[text()='处置意见：']/following-sibling::textarea")
    # 处置前图片
    handle_before_photo = (By.XPATH, "//*[text()='处置前图片：']/following-sibling::span//input")
    # 处置后图片
    handle_after_photo = (By.XPATH, "//*[text()='处置后图片：']/following-sibling::span//input")
    # 处置意见取消
    handle_opining_cancel = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div/div[4]/div[15]/button/div/div[2]/div[1]")
    # 处置意见确定
    handle_opining_sure = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div/div[4]/div[15]/button/div/div[2]/div[2]")


if __name__ == "__main__":
    s = SecondHandleCasePage()
    s.click_element(s.source_information_case)
    if s.find_ele(s.case_question_content).text == "测试":
        print("测试")
        s.click_element(s.handle)
        s.element_input_text(s.handle_opining, "测试")
        s.click_element(s.handle_opining_sure)

