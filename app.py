from flask import Flask, render_template, request
from repository.login_dao import insert_user, select_user
from models.login_dto import Login
from controller.home_controller import *
from controller.login_controller import *
from controller.registration_controller import *
from controller.deletion_controller import delete_user_account
from controller.request_controller import *
from controller.manager_controller import *

app = Flask(__name__)

@app.route('/', methods=["GET"])
def landing_page():
    return get_homepage()

@app.route('/login', methods=["GET"])
def login_page():
    return get_login_page()

@app.route('/login/input', methods=["POST"])
def user_login():
    print(request.form)
    return check_user_login(request.form)

@app.route('/registration')
def registration_page():
    return get_registration_page()

@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)

@app.route('/deletion/<username>')
def delete_existing_user(username):
    return delete_user_account(username)

@app.route('/request/<username>')
def request_users_page(username):
    return get_request_page(username)

@app.route('/request/<username>/create', methods=["POST"])
def request_create_page(username):
    print("Hello 10000")
    return request_user_input(username,request.form)



#----------------
#Employee Pages
#----------------
@app.route('/login/employee', methods=["GET"])
def employee_login_page():
    return get_employee_login_page()


@app.route('/login/employee_login/input', methods=["GET", "POST"])
def employee_request_page():
    print(request.form)
    return check_user_login_employee(request.form)

@app.route('/cancel_request/<request_id>')
def cancel_request_page(request_id):
    return cancel_request(request_id, "employee_view_request.html")

@app.route('/employee_request/<username>')
def employ_request_users_page(username):
    return get_employee_request_page(username)

@app.route('/employee_account_page/<username>')
def go_to_employee_account_page(username):
    return get_employee_account_page(username)

@app.route('/employee_view_request/<username>')
def employee_view_request_users_page(username):
    return get_employee_view_request(username)


#----------------
#Manager Pages
#----------------
@app.route('/login/manager', methods=["GET"])
def manager_login_page():
    return get_manager_login_page()

@app.route('/login/manager/manager_account_page.html', methods=["POST"])
def manager_request_page():
    print(request.form)
    return check_user_login(request)


@app.route('/cancel_request_manager/<request_id>')
def cancel_request_manager_page(request_id):
    return cancel_request(request_id, "manager_view_request.html")

if __name__ == "__main__":
    app.run(debug=True)