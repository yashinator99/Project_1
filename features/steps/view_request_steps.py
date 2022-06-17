from behave import *

@given(u'emp user2 on login page')
def step_user2_on_login_page(context):
    context.driver.get('http://127.0.0.1:5000/login/employee')


@when(u'emp user2 inputs username {username}')
def step_user2_inputs_username(context, username):
    context.view_request.login_username().send_keys(username)


@when(u'emp user2 inputs password {password}')
def step_user2_inputs_password(context, password):
    context.view_request.login_password().send_keys(password) 


@when(u'emp user2 clicks submit on login page')
def step_user2_clicks_on_submit_on_login_page(context):
    context.view_request.click_submit().click()


@then(u'emp user2 is on account page')
def step_user2_on_account_page(context):
    assert context.driver.title == "Employee account page"


@when(u'emp user2 clicks on view previous requests')
def step_user2_clicks_on_request_reimbursement(context):
    context.view_request.employee_clicks_view_previous_request().click()       


@then(u'emp user2 is on view previous request page')
def step_user2_on_view_previous_request_page(context):
    assert context.driver.title == "View Request"       


@when(u'emp user2 clicks on cancel request')
def step_user2_clicks_on_cancel_request(context):
    context.view_request.employee_clicks_cancel_request().click() 


@then(u'emp user2 should be on view request page with request status updated to cancelled')   
def step_user2_on_view_request_page_with_updated_status(context):
    assert context.driver.title == "View Request"