from behave.runner import Context
from selenium import webdriver
from POM.login import Loginpage
from POM.homepage import Homepage
from POM.request import Request
from POM.view_request import View_request

def before_all(context: Context):
    # We need to add a driver to the context

    context.driver = webdriver.Chrome('Drivers/chromedriver.exe')
    # We need to add all POMS to the context
    context.homepage = Homepage(context.driver)
    context.login = Loginpage(context.driver)
    context.request = Request(context.driver)
    context.view_request = View_request(context.driver)
    # We add an implicit wait to work with latency issues
    #context.driver.implicitly_wait(1)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()