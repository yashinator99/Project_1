from behave import *

@given(u'I am on employee login page')
def step_employee_on_employee_login_page(context):
    context.driver.get('http://127.0.0.1:5000/login/employee')

@given(u'I am on manager login page')
def step_manager_on_manager_login_page(context):
    context.driver.get('http://127.0.0.1:5000/login/manager')


@when(u'I input a valid username {username}')
def step_employee_inputs_valid_username(context, username):
    context.login.login_username().send_keys(username)


@when(u'I input a valid password {password}')
def step_employee_inputs_valid_password(context, password):
    context.login.login_password().send_keys(password)

@when(u'I click on the Submit button')
def step_employee_clicks_submit_button(context):
    context.login.click_submit().click()


@then(u'I should be on the page with title Employee account page')
def step_employee_is_routed_to_employee_account_page(context):
    assert context.driver.title == "Employee account page"

@then(u'I should be on the page with title Manager account page')
def step_manager_is_routed_to_manager_account_page(context):
    assert context.driver.title == "Manager account page"