from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Request:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_username(self):
        return self.driver.find_element(By.ID, "username")

    def login_password(self):
        return self.driver.find_element(By.ID, "password")

    def click_submit(self):
        return self.driver.find_element(By.ID, "submit")

    def employee_clicks_request_reimbursement(self):
        return self.driver.find_element(By.ID, "request_reim")

    def employee_request_desc(self):
        return self.driver.find_element(By.ID, "request_desc")

    def employee_request_amount(self):
        return self.driver.find_element(By.ID, "request_amount")

    def employee_submits_request(self):
        return self.driver.find_element(By.ID, "submit")

    #Manager
    def clicks_request_reimbursement(self):
        return self.driver.find_element(By.ID, "request_reim")

    def request_desc(self):
        return self.driver.find_element(By.ID, "request_desc")

    def request_amount(self):
        return self.driver.find_element(By.ID, "request_amount")

    def submits_request(self):
        return self.driver.find_element(By.ID, "submit")