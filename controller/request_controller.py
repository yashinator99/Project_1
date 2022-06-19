from flask import render_template
from service.request_service import *
from service.deletion_service import prep_user_id

#employee request

def get_employee_request_page(username):
    return render_template("employee_request.html", username=username)

def get_employee_account_page(username):
    return render_template("employee_account_page.html", username=username)

def get_employee_view_request(username):
    user_id = prep_user_id(username)
    request_info = get_view_request(user_id)
    print(request_info)
    return render_template("employee_view_request.html", username=username, info=request_info)

def request_user_input(username,register_input):
    user_id = prep_user_id(username)
    role = user_role(user_id)
    print(role)
    if validate_request_service(register_input):
        request_id = create_request(user_id, register_input)
        if request_id is not None:
            if role == "manager":
                return render_template("manager_account_page.html", username=username)
            else:
                return render_template("employee_account_page.html", username=username)
    else:
        if role == "manager":
            return render_template("failed_request_manager.html", username=username)
        else:
            return render_template("failed_request.html", username=username)

#manager request

def get_manager_request_page(username):
    return render_template("manager_request.html", username=username)
# New
def get_manager_view_request(username):
    user_id = prep_user_id(username)
    request_info = get_view_request(user_id)
    print(request_info)
    return render_template("manager_view_request.html", username=username, info=request_info)
# New
def get_manager_view_all_request(username):
    request_info = get_view_all_request()
    print(request_info)
    return render_template("manager_view_all_request.html", username=username, info=request_info)

# New
def get_manager_account_page(username):
    return render_template("manager_account_page.html", username=username)

# New
def get_manager_view_accepted_page(username):
    request_info = get_view_request_status("accepted")
    print(request_info)
    return render_template("manager_view_accepted_request.html", username=username, info=request_info)

# rejected
def get_manager_view_rejected_page(username):
    request_info = get_view_request_status("rejected")
    print(request_info)
    return render_template("manager_view_rejected_request.html", username=username, info=request_info)


# request info

def cancel_request(username, request_id, page):
    update_status(request_id,"cancelled")
    user_id = get_user_id_from_request_id(request_id)
    request_info = get_view_request(user_id)
    return render_template(page, username=username, info=request_info)

def accept_request(username, request_id, page):
    update_status(request_id,"accepted")
    user_id = get_user_id_from_request_id(request_id)
    request_info = get_view_request(user_id)
    return render_template(page, username=username,info=request_info)

def reject_request(username, request_id, page):
    update_status(request_id,"rejected")
    user_id = get_user_id_from_request_id(request_id)
    request_info = get_view_request(user_id)
    return render_template(page, username=username,info=request_info)


