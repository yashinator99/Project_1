from flask import render_template
from service.login_service import check_login,check_login_role


def get_login_page():
    return render_template("login.html")

def check_user_login(login_input):
    user_login = check_login(login_input)

    if user_login is None:
        return render_template("failed_login.html") #change this
    else:
        return render_template("account_page.html", username=user_login.username)

def get_employee_login_page():
    return render_template("employee_login.html")

def check_user_login_employee(login_input):
    user_login = check_login_role(login_input,"employee")

    if user_login is None:
        return render_template("failed_login.html")
    else:
        return render_template("employee_account_page.html", username=user_login.username)