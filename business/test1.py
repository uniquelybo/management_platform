# -*- coding: utf-8 -*-
import sys
sys.path.append("D:\\pycharm\projects\\management_platform\\page")
from page.dispatchPage import DispatchPage
import pandas as pd
import read_excel
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    # 登录
    # data = pd.read_excel("C:/Users/fcy-034/Desktop/自动化测试用例.xlsx", sheet_name="user")
    # dicts = read_excel.read_excel(data)
    # print(dicts["data_0"].get("username"), str(dicts["data_0"].get("password")), str(dicts["data_0"].get("code")))
    # # for dic in dicts:
    # #     print(dic)
    # login = LoginPage()
    # login.user_login(dicts["data_0"].get("username"), str(dicts["data_0"].get("password")), str(dicts["data_0"].get("code")))
    # 录入
    data = pd.read_excel("C:/Users/fcy-034/Desktop/自动化测试用例.xlsx", sheet_name="input_data")
    dicts = read_excel.read_excel(data)
    # print(dicts)
    # messageEntryPage = MessageEntryPage()
    # messageEntryPage.input_massage(dicts["data_0"])
    disp = DispatchPage()
    # 派遣
    # disp.is_massage(dicts["data_0"])
    disp.user_data_eq(dicts["data_0"])

