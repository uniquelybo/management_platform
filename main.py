from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests

if __name__ == '__main__':
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # chrome_driver = "D:\chromedriver_win32\chromedriver.exe"
    # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    # print(driver.title)
    # wait = WebDriverWait(driver, 10)
    # username = driver.find_element_by_id("account")
    # passsword = driver.find_element_by_id("password")
    # code = driver.find_element_by_id("code")
    # login_button = driver.find_element_by_xpath("//*[@type='submit']")
    # username.send_keys("shouliyuanAccount")
    # passsword.send_keys("123456")
    # code.send_keys("1234")
    # login_button.click()
    #
    # driver.quit()
    headers = {
        "Cookie": "JSESSIONID=C0031CA9CCFB893D2419FF4F46A6F945",
        "Host": "zhgl.tyzhcs.cn",
        "Origin": "http://zhgl.tyzhcs.cn",
        "Proxy-Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    data = {"content": "",
            "source": "",
            "status": 1,
            "beginTime": "",
            "endTime": "",
            "aType": "",
            "street": "",
            "community": "",
            "pageSize": 10,
            "pageNo": 1
    }
    response = requests.get(url="http://zhgl.tyzhcs.cn/operation/one/page", json=data, headers=headers)
    print(response.text)
