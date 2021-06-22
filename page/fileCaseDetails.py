from selenium.webdriver.common.by import By
from basePage import BasePage


class FileCaseDetails(BasePage):
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
    # 取消
    cancel = (By.XPATH, "//*[text()=' 取消 ']")
    # 确定
    file_case = (By.XPATH, "//*[text()=' 立案 ']")
    # 立案意见
    case_opining = (By.XPATH, "//*[text()='立案意见']/../following-sibling::div[1]//textarea")
    # 常用语
    common_words = (By.XPATH, "//*[text()='常用语']")
    # 常用语内容
    common_content = (By.XPATH, "//*[text()=' 常用语内容 ']/../../../following-sibling::ul[1]//li[1]/div[2]/span")
    # 立案取消
    file_case_cancel = (By.XPATH, "//*[text()='常用语']/../../../following-sibling::div[1]/div[1]")
    # 立案确定
    file_case_sure = (By.XPATH, "//*[text()='常用语']/../../../following-sibling::div[1]/div[2]")

    # 根据是否保密判断是否显示上报人信息
    def Judgment_secret(self):
        if self.find_ele(self.secret_value).text == "是":
            if self.find_ele(self.user_name).text != "***":
                print("name, False")
            print(self.find_ele(self.user_phone).text)
            if self.find_ele(self.user_phone).text != "***":
                print("phone, False")
            print(self.find_ele(self.user_sex).text)
            if self.find_ele(self.user_sex).text != "***":
                print("sex, False")
        # if self.find_ele(self.secret_value).text == "否":
        #     if self.find_ele(self.user_name).text != "——":
        #         print("name, False")
        #     print(self.find_ele(self.user_phone).text)
        #     if self.find_ele(self.user_phone).text != "——":
        #         print("phone, False")
        #     print(self.find_ele(self.user_sex).text)
        #     if self.find_ele(self.user_sex).text != "——":
        #         print("sex, False")
