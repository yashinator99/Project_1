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


#manager

#view previous request
@when(u'I click on manager view previous requests')
def step_manger_clicks_on_request_reimbursement(context):
    context.view_request.manager_clicks_view_previous_request().click()


@then(u'I am on manager view previous request page')
def step_manager_on_view_previous_request_page(context):
    assert context.driver.title == "Manager View Request"

#canceling request
@when(u'I click on cancel request')
def step_manager_clicks_on_cancel_request(context):
    context.view_request.manager_clicks_cancel_request().click()


@then(u'I should be on view request page with request status updated to cancelled')
def step_manager_on_view_request_page_with_updated_status(context):
    assert context.driver.title == "Manager View Request"

#view accept request
@when(u'I click on manager view accepted requests')
def step_manager_clicks_on_accept_request(context):
    context.view_request.manager_clicks_view_acccepted_request().click()


@then(u'I am on manager view accepted request page')
def step_manager_on_view_accept_request_page(context):
    assert context.driver.title == "View All Accepted Request"

#view rejected request
@when(u'I click on manager view rejected requests')
def step_manager_clicks_on_rejected_request(context):
    context.view_request.manager_clicks_view_rejected_request().click()


@then(u'I am on manager view rejected request page')
def step_manager_on_view_previous_request_page(context):
    assert context.driver.title == "View All Rejected Request"

#view all request
@when(u'I click on manager view all requests')
def step_manager_clicks_on_all_request(context):
    context.view_request.manager_clicks_view_all_previous_request().click()


@then(u'I am on manager view all request page')
def step_manager_on_view_all_request_page(context):
    assert context.driver.title == "View All Request"

