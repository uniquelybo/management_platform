import time

from selenium.webdriver.common.by import By
from basePage import BasePage


class DispatchPage(BasePage):
    # 待派遣案件
    wait_dispatch_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[1]")
    # 待审核案件
    wait_audit_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[2]")
    # 回退案件
    back_case = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[4]")
    # 找测试数据
    test_case_num = (By.XPATH, "//tr/td[text()='其他']/preceding-sibling::td[1]")
    # 问题内容
    question_content = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/ul[3]/li[2]/p/span")
    # 派遣
    dispatch_button = (By.XPATH, "//*[text()='派遣']")
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
    # 派遣
    dispatch = (By.XPATH, "//*[text()=' 派遣 ']")
    # 取消
    cancel = (By.XPATH, "//*[text()=' 取消 ']")
    # 派遣单位
    dispatch_name = (By.XPATH, "//*[text()=' 派遣单位 ']/following-sibling::div[1]/input")
    # 查询派遣单位
    dispatch_search = (By.XPATH, "//*[text()='处置部门(测试)']")
    # 一级派遣单位
    one_dispatch = (By.XPATH, "//div[text()='处置部门(测试)']")
    # 选择处置员
    dispatch_person = (By.XPATH, "//div[text()='处置部门(测试)']/following-sibling::div[1]/div/div[1]/div[2]/p")
    # 派遣取消
    dispatch_cancel = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div/div/div[4]/button/div/div[2]/div[1]")
    # 派遣确定
    dispatch_sure = (By.XPATH, "//section/section/main/div[2]/div[2]/div/div/div/div/div/div[4]/button/div/div[2]/div[1]")
    # 派遣意见
    dispatch_opining = (By.XPATH, "//*[text()=' 派遣意见 ']/following-sibling::textarea")

    def is_massage(self, data):
        area = data["所属街办"] + "，" + data["所属社区"]
        ele_path = "//td[text()='—']/following-sibling::td[1][text()='其他']" \
                       "/following-sibling::td[2][text()='%s']" \
                       "/following-sibling::td[5][text()='%s']" \
                       "/following-sibling::td[1][text()='%s']" \
                       "/following-sibling::td[1][text()='%s']" \
                       % (area, data["一类类型"], data["二类类型"], data["三类类型"])
        element = (By.XPATH, ele_path)
        self.find_element(element).click()

    def user_data_eq(self, data):
        self.find_element(self.user_data).click()
        if self.find_element(self.secret_value).text == "是":
            print("比较内容")
            print(self.find_element(self.user_name).text)
            if self.find_element(self.user_name).text != "***":
                print("name, False")
            print(self.find_element(self.user_phone).text)
            if self.find_element(self.user_phone).text != "***":
                print("phone, False")
            print(self.find_element(self.user_sex).text)
            if self.find_element(self.user_sex).text != "***":
                print("sex, False")
        elif self.find_element(self.secret_value).text == "否":
            print("比较内容")
            print(self.find_element(self.user_name).text)
            if self.find_element(self.user_name).text != data['上报人姓名'] | self.find_element(self.user_name).text != "—":
                print("name, False")
            print(self.find_element(self.user_phone).text)
            if self.find_element(self.user_phone).text != data['手机号'] | self.find_element(self.user_phone).text != "—":
                print("phone, False")
            print(self.find_element(self.user_sex).text)
            if self.find_element(self.user_sex).text != data['性别'] | self.find_element(self.user_sex).text != "—":
                print("sex, False")
        else:
            print(self.find_element(self.secret_value).text)


if __name__ == "__main__":
    d = DispatchPage()
    # d.is_massage()
    # d.click_element(d.user_data)
    # d.click_element(d.user_data)
    # print(d.find_ele(d.secret_value).text)


    # d.click_element(d.cancel)


    d.find_element(d.dispatch_name).send_keys("处置部门(测试)")
    time.sleep(1)
    d.find_element(d.dispatch_search).click()
    d.find_element(d.one_dispatch).click()
    time.sleep(0.5)
    d.find_element(d.dispatch_person).click()
    d.find_element(d.dispatch_opining).send_keys("测试")


