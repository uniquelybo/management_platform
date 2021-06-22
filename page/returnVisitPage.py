from selenium.webdriver.common.by import By
from basePage import BasePage


class ReturnVisitPage(BasePage):
    # 状态
    state = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div[2]/button/div/div[1]/span/div/div[1]/div/div[2]/div[4]/div/div[1]/div/div/div")
    # 未接通
    # disconnected = (By.XPATH, "//ul[@role='listbox']/li[text()=' 未接通 ']")
    # 回访录入
    returnVisit_input = (By.XPATH, "//button[text()='回访录入']")
    # 满意
    satisfied = (By.XPATH, "//span[text()='满意']")
    # 不满意
    not_satisfied = (By.XPATH, "//span[text()='不满意']")
    # 不回访
    not_return_visit = (By.XPATH, "//span[text()='不回访']")
    # 结果模糊、敷衍
    box1 = (By.XPATH, "//span[text()='结果模糊、敷衍']/preceding-sibling::span[1]/input")
    # 推卸责任不予办理
    box2 = (By.XPATH, "//span[text()='推卸责任不予办理']/preceding-sibling::span[1]/input")
    # 内容回复
    return_input_opining = (By.XPATH, "//textarea[@placeholder='回复内容/结果模糊/推卸责任']")
    # 确定
    sure = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div[2]/button/div/div[2]/div[2]")
    # 取消
    cancel = (By.XPATH, "//section/main/div[2]/div[2]/div/div/div[2]/button/div/div[2]/div[1]")

    # 电话回访
    phone_returnVisit = (By.XPATH, "//button[text()='电话回访']")
    # 换绑
    rebiding = (By.XPATH, "//button[text()='换绑']")
    # 当前分机号
    now_phone_num = (By.XPATH, "//button[text()='换绑']/preceding-sibling::p[1]/span")
    # 输入电话号码
    input_phone_num = (By.XPATH, "//span[text()='输入电话号码:']/following-sibling::input[1]")

    # 是否外地号码
    def is_foreign_number(self, value):
        if value != "是" or value != "否":
            x = "//span[text()='是否外地号码:']/following-sibling::div[1]//span[text()=' %s ']/preceding-sibling::span[1]/input" % value
            is_value = (By.XPATH, x)
            print(is_value)
            return self.find_element(is_value)


if __name__ == "__main__":
    r = ReturnVisitPage()
    # r.click_element(r.state)
    # r.click_element(r.cancel)
    # print(r.phone_returnVisit)
    # print(type(r.phone_returnVisit))
    # r.find_element(r.returnVisit_input).click()
    # v = r.find_element(r.box2).is_selected()
    # print(v)
    # r.find_element(r.return_input_opining).send_keys("测试")
    r.is_foreign_number("否").click()
    print(r.is_foreign_number("否").is_selected())

