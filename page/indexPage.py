import time

from basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class IndexPage(BasePage):
    first_page = (By.XPATH, "//*[text()='首页']")
    operating_table = (By.XPATH, "//*[text()='操作台']")
    my_to_deal_with = (By.XPATH, "//*[text()='我的待处理']")
    my_to_deal_with_case = (By.XPATH, "//*[text()='我的待处理案件']/..")
    tow_wait_handle_case = (By.XPATH, "//*[text()='二级待处理案件']/..")
    user_account = (By.XPATH, "//section/section/div/header/div/div/div/span/span")
    user_logout = (By.XPATH, "//*[text()='退出登录']")
    user_logout_sure = (By.XPATH, "//*[text()='确 定']/..")


if __name__ == "__main__":
    print("1")
    i = IndexPage()
    i.click_element(i.operating_table)
    time.sleep(0.5)
    i.click_element(i.tow_wait_handle_case)
    # actionChain = ActionChains(i.driver)
    # time.sleep(2)
    # i.click_element(i.user_account)
    # actionChain.move_to_element(i.find_ele(i.user_logout)).perform()
    # time.sleep(1)
    # i.click_element(i.user_logout)
    # i.click_element(i.user_logout_sure)