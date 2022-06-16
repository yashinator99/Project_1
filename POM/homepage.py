from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    def employee_login_link(self):
        return self.driver.find_element(By.ID, "employee_login_link")

    def manager_login_link(self):
        return self.driver.find_element(By.ID, "manager_login_link")

