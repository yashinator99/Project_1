from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_username(self):
        return self.driver.find_element(By.ID, "username")

    def login_password(self):
        return self.driver.find_element(By.ID, "password")

    def click_submit(self):
        return self.driver.find_element(By.ID, "submit")