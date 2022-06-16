from behave import *

@given(u'I am on the homepage')
def step_employee_on_homepage(context):
    context.driver.get('http://127.0.0.1:5000/')

@when(u'I click on the employee login link')
def step_employee_clicks_on_login_link(context):
    context.homepage.employee_login_link().click()

@when(u'I click on the manager login link')
def step_manager_clicks_on_login_link(context):
    context.homepage.manager_login_link().click()


@then(u'I should be routed to the employee login page')
def step_employee_is_routed_to_employee_login_page(context):
    assert context.driver.title == "Employee Login"

@then(u'I should be routed to the manager login page')
def step_manager_is_routed_to_manager_login_page(context):
    assert context.driver.title == "Manager Login"
