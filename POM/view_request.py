from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class View_request:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_username(self):
        return self.driver.find_element(By.ID, "username")

    def login_password(self):
        return self.driver.find_element(By.ID, "password")

    def click_submit(self):
        return self.driver.find_element(By.ID, "submit")

    def employee_clicks_view_previous_request(self):
        return self.driver.find_element(By.ID, "view prev req")

    def employee_clicks_cancel_request(self):
        return self.driver.find_element(By.ID, "cancel_request")

    def manager_clicks_view_previous_request(self):
        return self.driver.find_element(By.ID, "view-prev-req")

    def manager_clicks_cancel_request(self):
        return self.driver.find_element(By.ID, "cancel_request")

    def manager_clicks_view_all_previous_request(self):
        return self.driver.find_element(By.ID, "view-all-req")

    def manager_clicks_view_acccepted_request(self):
        return self.driver.find_element(By.ID, "view-accepted-req")

    def manager_clicks_view_rejected_request(self):
        return self.driver.find_element(By.ID, "view-rejected-req")

    def manager_clicks_accept_request(self):
        return self.driver.find_element(By.ID, "accpeted_request")

    def manager_clicks_reject_request(self):
        return self.driver.find_element(By.ID, "rejected_request")