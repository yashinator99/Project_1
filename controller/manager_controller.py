from flask import render_template
from service.login_service import check_login,check_login_role


def get_manager_login_page():
    return render_template("manager_login.html")

def check_user_login_manager(login_input):
    user_login = check_login_role(login_input, "manager")

    if user_login is None:
        return render_template("failed_login.html") #change this
    else:
        return render_template("manager_account_page.html", username=user_login.username)