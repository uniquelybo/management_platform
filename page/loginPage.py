from basePage import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    username = (By.ID, "account")
    password = (By.ID, "password")
    # code = (By.ID, "code")
    login_button = (By.XPATH, "//*[@type='submit']")

    def user_login(self, username, password, code):
        self.find_element(self.username).clear()
        self.find_element(self.username).send_keys(username)
        self.find_element(self.password).clear()
        self.find_element(self.password).send_keys(password)
        self.find_element(self.login_button).click()


# if __name__ == "__main__":
#     l = LoginPage()
#     l.user_login("shouliyuanAccount", "123456", "1234")
