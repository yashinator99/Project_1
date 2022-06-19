from behave import *

@given(u'emp user1 on login page')
def step_user1_on_login_page(context):
    context.driver.get('http://127.0.0.1:5000/login/employee')

@when(u'emp user1 inputs username {username}')
def step_user1_inputs_username(context, username):
    context.request.login_username().send_keys(username)


@when(u'emp user1 inputs password {password}')
def step_user1_inputs_password(context, password):
    context.request.login_password().send_keys(password)


@when(u'emp user1 clicks submit on login page')
def step_user1_clicks_on_submit_on_login_page(context):
    context.request.click_submit().click()

@then(u'emp user1 is on account page')
def step_user1_on_account_page(context):
    assert context.driver.title == "Employee account page" #(u'http://127.0.0.1:5000/employee_account_page/')


@when(u'emp user1 clicks on request reimbursement')
def step_user1_clicks_on_request_reimbursement(context):
    context.request.employee_clicks_request_reimbursement().click()


@then(u'emp user1 is on request reimbursement page')
def step_user1_on_reimbursement_page(context):
    assert context.driver.title == "Employee Request Page"


@when(u'emp user1 inputs request description {description}')
def step_user1_inputs_description(context, description):
    context.request.employee_request_desc().send_keys(description)


@when(u'emp user1 inputs request amount {amount}')
def step_user1_inputs_amount(context, amount):
    context.request.employee_request_amount().send_keys(amount)


@when(u'emp user1 clicks submit on request reimbursement page')
def step_user1_clicks_submit_on_request_page(context):
    context.request.employee_submits_request().click()


@then(u'emp user1 should be back on account page')
def step_user1_should_be_back_on_account_page(context):
    assert context.driver.title == "Employee account page"


#### Manager
@when(u'I click on request reimbursement')
def step_clicks_on_request_reimbursement(context):
    context.request.clicks_request_reimbursement().click()


@then(u'I am on request reimbursement page')
def step_on_reimbursement_page(context):
    assert context.driver.title == "Manager Request Page"


@when(u'I input request description {description}')
def step_inputs_description(context, description):
    context.request.request_desc().send_keys(description)


@when(u'I input request amount {amount}')
def step_inputs_amount(context, amount):
    context.request.request_amount().send_keys(amount)


@when(u'I click submit on request reimbursement page')
def step_clicks_submit_on_request_page(context):
    context.request.submits_request().click()


@then(u'I should be back on account page')
def step_should_be_back_on_account_page(context):
    assert context.driver.title == "Manager account page"