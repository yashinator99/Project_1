from models.request_dto import Request
from repository.login_dao import insert_user, get_user_id, get_user_role
from repository.user_info_dao import insert_user_info
from repository.request_dao import *
from service.validation_service import validate_login, validate_request_desc, validate_request_amount
# To register
# Valid Username and Password
# Valid first name and last name

#def validate_request_service(input):
#    request_dto = Request(0, input.get("request_desc"), input.get("request_amount"), "pending")
#    return request_dto.validate_employee_request()
def validate_request_service(input):
    return validate_request_desc(input.get("request_desc")) and validate_request_amount(input.get("request_amount"))
# working impl
def validate_login_service(input_dict):
    return validate_login((input_dict["username"], input_dict["password"])), ((input_dict["role"]))

def create_request(user_id, input):
    return insert_user_request(user_id, input.get("request_desc"), int(input.get("request_amount")))

def get_view_request(user_id):
    return get_request(user_id)

# New
def get_view_all_request():
    return get_all_request()

def get_view_request_status(status):
    return get_status_request(status)

def update_status(request_id, status):
    return update_request(request_id, status)

def user_role(user_id):
    return get_user_role(user_id)