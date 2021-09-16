import time

from selenium import webdriver

URL = 'https://www.saucedemo.com/'


def login_saucedemo():
    driver = webdriver.Chrome('driver/chromedriver.exe')
    driver.get(URL)
    login_user = driver.find_element_by_id("user-name")
    login_user.send_keys("standard_user")
    time.sleep(2)
    login_password = driver.find_element_by_id("password")
    login_password.send_keys("secret_sauce")
    time.sleep(2)
    login = driver.find_element_by_id('login-button')
    login.click()
    time.sleep(2)
    driver.close()


if __name__ == "__main__":
    login_saucedemo()
