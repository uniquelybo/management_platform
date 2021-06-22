import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from basePage import BasePage
import pandas as pd


class MessageEntryPage(BasePage):
    # 上报人信息
    message_entry = (By.XPATH, "//*[text()='信息录入']")
    name = (By.XPATH, "//*[text()='上报人姓名']/../following-sibling::div[1]//input")
    phone = (By.XPATH, "//*[text()='手机号']/../following-sibling::div[1]//input")
    sex = (By.XPATH, "//*[text()='性别']/../following-sibling::div[1]//span")
    secrets = (By.XPATH, "//*[text()='保密']/../following-sibling::div[1]//span")
    # 案件信息
    street_office = (By.XPATH, "//*[text()='所属街办']/../following-sibling::div[1]//span")
    community = (By.XPATH, "//*[text()='所属社区']/../following-sibling::div[1]//span")
    source_information = (By.XPATH, "//*[text()='信息来源']/../following-sibling::div[1]//span")
    case_type = (By.XPATH, "//*[text()='案件类型']/../following-sibling::div[1]//span")
    one_type = (By.XPATH, "//*[text()='一类类型']/../following-sibling::div[1]//span")
    tow_type = (By.XPATH, "//*[text()='二类类型']/../following-sibling::div[1]//span")
    three_type = (By.XPATH, "//*[text()='三类类型']/../following-sibling::div[1]//span")
    processing_period1 = (By.XPATH, "//*[text()='处理期限']/../following-sibling::div[1]//span/div[1]//input")
    processing_period2 = (By.XPATH, "//*[text()='处理期限']/../following-sibling::div[1]//span/div[2]//input")
    collection_site = (By.XPATH, "//*[text()='采集地点']/../following-sibling::div[1]//input")
    question_description = (By.XPATH, "//*[text()='问题描述']/../following-sibling::div[1]//textarea")
    map_chooice = (By.XPATH, "//*[text()='地图选择']")
    search_Coordinates = (By.XPATH, "//*[text()=' 按坐标搜索 ']")
    search_Coordinates_value = (By.XPATH, "//*[text()='搜索']/preceding-sibling::input[1]")
    search = (By.XPATH, "//*[text()='搜索']")
    map_enter = (By.XPATH, "//*[text()='确认'][@class='submitbtn']")
    """
    112.55042,37.87088
    """
    case_map = (By.XPATH, "//*[text()='案件上报图']/../following-sibling::div[1]//input")
    cancel = (By.XPATH, "//*[text()=' 取消 ']")
    sure = (By.XPATH, "//*[text()=' 提交 ']")
    # 最后取消
    last_cancel = (By.XPATH, "//*[text()='是否对内容进行发布？']/following-sibling::div[1]/button[1]")
    # 最后确认
    last_sure = (By.XPATH, "//*[text()='是否对内容进行发布？']/following-sibling::div[1]/button[2]")
    # 未填项提示信息
    no_input_message = (By.XPATH, "/html/body/div[2]/span/div/div/div/span")

    # 发布案件
    def release_case(self):
        self.find_element(self.sure).click()
        self.find_element(self.last_sure).click()

    # 最后取消发布
    def last_cancel_release(self):
        self.find_element(self.sure).click()
        self.find_element(self.last_cancel).click()

    # 选择值
    def chooice_value(self, value):
        value = (By.XPATH, "//*[@role='listbox']/li[text()=' %s ']" % value)
        self.find_element(value).click()

    # 选择性别
    def chooice_sex(self, value):
        if value == "":
            return
        self.find_element(self.sex).click()
        self.chooice_value(value)

    # 选择是否保密
    def chooice_secrets(self, value):
        if value == "":
            return
        self.find_element(self.secrets).click()
        self.chooice_value(value)

    # 选择所属街办
    def chooice_street_office(self, value):
        if value == "":
            return
        self.find_element(self.street_office).click()
        self.chooice_value(value)

    # 选择社区
    def chooice_community(self, value):
        if value == "":
            return
        self.find_element(self.community).click()
        self.chooice_value(value)

    # 选择信息来源
    def chooice_source_information(self, value):
        if value == "":
            return
        self.find_element(self.source_information).click()
        self.chooice_value(value)

    # 选择案件类型
    def chooice_case_type(self, value):
        if value == "":
            return
        self.find_element(self.case_type).click()
        self.chooice_value(value)

    # 选择一类类型
    def chooice_one_type(self, value):
        if value == "":
            return
        self.find_element(self.one_type).click()
        self.chooice_value(value)

    # 选择二类类型
    def chooice_tow_type(self, value):
        if value == "":
            return
        self.find_element(self.tow_type).click()
        self.chooice_value(value)

    # 选择三类类型
    def chooice_three_type(self, value):
        if value == "":
            return
        self.find_element(self.three_type).click()
        self.chooice_value(value)

    # 地图选择
    def chooice_map_chooice(self, value):
        if value == "":
            return
        self.find_element(self.map_chooice).click()
        self.find_element(self.search_Coordinates).click()
        time.sleep(0.5)
        self.find_element(self.search_Coordinates_value).send_keys(value)
        time.sleep(0.5)
        self.find_element(self.search).click()
        time.sleep(0.5)
        self.find_element(self.map_enter).click()

    # 上传图片
    def upload_photo(self, value):
        if value == "":
            return
        # self.element_input_text(self.case_map, data.get("photo"))
        value = value.split(",")
        for v in value:
            self.find_element(self.case_map).send_keys(v)
        print(value)

    def input_massage(self, data):
        self.find_element(self.name).clear()
        self.find_element(self.name).send_keys(data["上报人姓名"])
        self.find_element(self.phone).clear()
        self.find_element(self.phone).send_keys(data["手机号"])
        self.chooice_sex(data["性别"])
        self.chooice_secrets(data["保密"])
        self.chooice_street_office(data["所属街办"])
        self.chooice_community(data["所属社区"])
        self.chooice_source_information(data["信息来源"])
        self.chooice_case_type(data["案件类型"])
        self.chooice_one_type(data["一类类型"])
        self.chooice_tow_type(data["二类类型"])
        self.chooice_three_type(data["三类类型"])
        self.find_element(self.processing_period1).clear()
        self.find_element(self.processing_period1).send_keys(Keys.CONTROL, 'a')
        self.find_element(self.processing_period1).send_keys(data["处理期限(天)"])
        self.find_element(self.processing_period2).clear()
        self.find_element(self.processing_period2).send_keys(Keys.CONTROL, 'a')
        self.find_element(self.processing_period2).send_keys(data["处理期限(小时)"])
        self.chooice_map_chooice(data["地图坐标"])
        self.find_element(self.question_description).clear()
        self.find_element(self.question_description).send_keys(data["问题描述"])
        self.upload_photo(data["上传图片"])
